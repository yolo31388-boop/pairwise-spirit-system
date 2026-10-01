"""法宝器灵 - 带9个bug"""
from dataclasses import dataclass, field
import random

@dataclass
class Spirit:
    sid: str
    name: str
    level: int
    quality: str
    slot_type: str
    skills: dict

class SpiritSystem:
    def __init__(self):
        self.spirits: dict[str, Spirit] = {}
        self.equipped = {}

    def attach(self, spirit_id, equip_level):
        spirit = self.spirits[spirit_id]
        # bug1: 不检查装备等级
        self.equipped[spirit_id] = True
        return True

    def get_atk_bonus(self, player_id):
        # bug2: 加法叠加
        total = 0
        for sid in self.equipped:
            total += self.spirits[sid].level * 10
        return total

    def get_skill_chance(self, spirit_id):
        # bug3: 固定概率
        return 0.3

    def upgrade(self, spirit_id, exp):
        # bug4: 只需经验
        self.spirits[spirit_id].level += 1
        return True

    def get_resonance(self, spirit_ids):
        # bug5: 只看数量
        if len(spirit_ids) >= 3:
            return {"bonus": 100}
        return {}

    def detach(self, spirit_id):
        # bug6: 不返还材料
        del self.equipped[spirit_id]
        return True

    def upgrade_quality(self, spirit_id):
        # bug7: 品质固定
        return False

    def feed(self, target_id, food_id):
        # bug8: 无品质限制
        self.upgrade(target_id, 100)
        del self.spirits[food_id]

    def can_attach_slot(self, spirit_id, slot):
        # bug9: 无槽位类型
        return True
