# backend/app/api/characters.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/list")
def list_characters():
    return {"message": "角色列表功能尚未實作"}