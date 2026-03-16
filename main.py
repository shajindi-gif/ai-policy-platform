from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Task
from agents import run_agent

app = FastAPI(title="AI Company Command Center")

Base.metadata.create_all(bind=engine)

class CommandRequest(BaseModel):
    command: str
    agent_name: str = "general_agent"

@app.get("/")
def root():
    return {"status": "ok", "message": "AI Company Command Center is running"}

@app.post("/command")
def create_command(req: CommandRequest, db: Session = Depends(get_db)):
    task = Task(
        command=req.command,
        status="running",
        agent_name=req.agent_name
    )
    db.add(task)
    db.commit()
    db.refresh(task)

    try:
        result = run_agent(req.command, req.agent_name)
        task.result = result
        task.status = "done"
        db.commit()
        db.refresh(task)
    except Exception as e:
        task.status = "failed"
        task.result = str(e)
        db.commit()
        db.refresh(task)

    return {
        "task_id": task.id,
        "status": task.status,
        "result": task.result
    }

@app.get("/tasks")
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).order_by(Task.id.desc()).all()
    return [
        {
            "id": t.id,
            "command": t.command,
            "status": t.status,
            "result": t.result,
            "agent_name": t.agent_name,
            "created_at": t.created_at
        }
        for t in tasks
    ]

@app.get("/task/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": task.id,
        "command": task.command,
        "status": task.status,
        "result": task.result,
        "agent_name": task.agent_name,
        "created_at": task.created_at,
        "updated_at": task.updated_at
    }
