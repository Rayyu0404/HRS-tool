# backend/app/api/stages.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/list")
def list_stages():
    return {"message": "關卡資料功能尚未實作"}
