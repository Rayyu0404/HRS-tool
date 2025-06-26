from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any
from app.core.battle_simulator import simulate_battle

router = APIRouter()

class Character(BaseModel):
    name: str
    atk: float
    multiplier: float

class Enemy(BaseModel):
    name: str
    hp: float
    resistance: float

@router.post("/run")
def run_simulation(team: List[Character], enemies: List[Enemy]) -> Dict[str, Any]:
    team_dicts = [c.dict() for c in team]
    enemy_dicts = [e.dict() for e in enemies]
    result = simulate_battle(team_dicts, enemy_dicts)
    return result
