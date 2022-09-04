from unittest import TestCase

from utils.PosUtils import (
    Pos, Scope, ProportionPos,
    get_proportion_pos, pos_distance
)


class TestPosUtils(TestCase):

    def test_pos(self):
        pos1 = Pos(x=123, y=456)
        pos2 = Pos(x=123, y=456)
        print(f"{pos1}")
        print(f"{pos2}")
        self.assertEqual(pos1, pos2)
        self.assertFalse(pos1 == (123, 456))

    def test_scope(self):
        pos1 = Pos(x=100, y=200)
        pos2 = Pos(x=200, y=400)
        scope1 = Scope(pos1, pos2)
        self.assertTrue(scope1.isin((150, 250)))
        self.assertFalse(scope1.isin((250, 250)))
        scope2 = Scope((100, 200), (200, 400))
        self.assertEqual(scope1, scope2)

    def test_proportion_pos(self):
        pro_pos = ProportionPos(0.5, 5)
        scope = Scope((0, 0), (1920, 1080))
        self.assertEqual(pro_pos.getPos(scope), Pos(960.0, 216.0))
        self.assertEqual(pro_pos.getPos(((0, 0), (1920, 1080))), Pos(960.0, 216.0))

        pos1, pos2 = get_proportion_pos(scope, (10, 5), (0.1, 20))
        self.assertEqual(pos1, Pos(192.0, 216.0))
        self.assertEqual(pos2, Pos(192.0, 54.0))

    def test_pos_distance(self):
        pos1 = Pos(x=3, y=0)
        pos2 = Pos(x=0, y=4)
        self.assertEqual(pos_distance(pos1, pos2), 5.0)
