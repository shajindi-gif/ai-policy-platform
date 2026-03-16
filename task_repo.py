from db import get_conn


def create_task(task_id: str, command: str, status: str = "PENDING"):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO tasks (task_id, command, status)
        VALUES (%s, %s, %s)
        """,
        (task_id, command, status),
    )
    conn.commit()
    cur.close()
    conn.close()


def update_task(task_id: str, status: str, result: str = None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE tasks
        SET status = %s, result = %s
        WHERE task_id = %s
        """,
        (status, result, task_id),
    )
    conn.commit()
    cur.close()
    conn.close()


def get_task(task_id: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT task_id, command, status, result, created_at
        FROM tasks
        WHERE task_id = %s
        """,
        (task_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def list_tasks():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT task_id, command, status, result, created_at
        FROM tasks
        ORDER BY created_at DESC
        """
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
