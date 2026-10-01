"""器灵测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import SpiritSystem, Spirit

class TestAttach:
    def test_equip_level_checked(self):
        ss = SpiritSystem()
        ss.spirits = {"s1": Spirit("s1","a",50,"epic","attack",{})}
        # 1级装备不应能附50级器灵
        assert not ss.attach("s1", 1), "装备等级未检查"

class TestResonance:
    def test_resonance_specific(self):
        ss = SpiritSystem()
        ss.spirits = {"s1": Spirit("s1","a",1,"common","attack",{}), "s2": Spirit("s2","b",1,"common","defense",{}), "s3": Spirit("s3","c",1,"common","support",{})}
        # 不同类型不应触发共鸣
        assert ss.get_resonance(["s1","s2","s3"]) == {}, "共鸣只看数量"
