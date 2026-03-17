import time
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from celery_app import celery_app
from task_repo import update_task


def run_task(task_id: str, command: str):
    update_task(task_id, "RUNNING")

    try:
        output = f"任务已执行：{command}"
        update_task(task_id, "SUCCESS", output)
    except Exception as e:
        update_task(task_id, "FAILED", str(e))
