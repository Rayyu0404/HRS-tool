from typing import List, Dict, Any
from .damage_formula import calculate_damage

def simulate_battle(team: List[Dict[str, Any]], enemies: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    基本模擬邏輯（暫定為一回合一角色動作，無速度順序處理）
    """
    log = []
    enemy_hp = [e["hp"] for e in enemies]

    for member in team:
        for i, enemy in enumerate(enemies):
            damage = calculate_damage(member, enemy)
            enemy_hp[i] -= damage
            log.append({
                "attacker": member["name"],
                "target": enemy["name"],
                "damage": damage,
                "enemy_hp": max(0, enemy_hp[i])
            })

    return {
        "result": "partial" if any(hp > 0 for hp in enemy_hp) else "win",
        "log": log
    }
