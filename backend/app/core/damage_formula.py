def calculate_damage(attacker: dict, enemy: dict) -> float:
    """
    超簡化公式：ATK × 技能倍率 × (1 - 敵人抗性)
    """
    atk = attacker.get("atk", 100)
    multiplier = attacker.get("multiplier", 1.0)
    res = enemy.get("resistance", 0.1)

    base = atk * multiplier
    return base * (1 - res)
