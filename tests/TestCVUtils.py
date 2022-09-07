from unittest import TestCase

from utils import CVUtils
from utils.ImageUtils import read_image, show_adapt


class TestCvUtils(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.template = read_image("images/template.jpg")
        cls.template_adjust = read_image("images/template_adjust.jpg")
        cls.target = read_image("images/target.jpg")
        cls.targets = read_image("images/targets.jpg")

    def test_match(self):
        self.assertTrue(CVUtils.match(self.target, self.template, 0.95))
        self.assertFalse(CVUtils.match(self.target, self.template, 1))

    def test_find(self):
        scope = CVUtils.find(self.target, self.template, 0.95)
        print(f"test_find:{scope}")

    def test_find_all(self):
        # 未去除临近点
        scopes = CVUtils.find_all(self.targets, self.template, 0.95)
        print(f"未去除临近点 scopes len is {len(scopes)}")
        # 去除临近点
        scopes = CVUtils.find_all(self.targets, self.template, 0.95, 15)
        print(f"已去除临近点 scopes len is {len(scopes)}")

    def test_find_knn(self):
        scope = CVUtils.find_knn(self.target, self.template_adjust)
        if scope is not None:
            mark_image = CVUtils.mark(self.target, [scope])
            show_adapt(mark_image)

    def test_find_color(self):
        # 存在的值
        self.assertEqual(CVUtils.find_color(self.template, (223, 147, 134)), (1, 1))
        self.assertEqual(CVUtils.find_color(self.template, (175, 136, 167)), (93, 23))
        # 不存在的值
        self.assertIsNone(CVUtils.find_color(self.template, (255, 255, 255)))

    def test_check_color(self):
        # 精确值
        self.assertTrue(CVUtils.check_color(self.template, (1, 1), (223, 147, 134)))
        # 错误值
        self.assertFalse(CVUtils.check_color(self.template, (1, 1), (223, 147, 135)))
        # 错误值-容差
        self.assertTrue(CVUtils.check_color(self.template, (1, 1), (223, 147, 135), 2))

    def test_match_mark(self):
        CVUtils.match_mark(self.target, self.template)
        CVUtils.match_marks(self.targets, self.template)
        CVUtils.match_mark_bfm(self.target, self.template_adjust)
        CVUtils.match_mark_knn(self.target, self.template_adjust)

    def test_find_multi_color(self):
        pos = CVUtils.find_multi_color(self.template, (102, 21, 62),
                                       [
                                           (-210, -10, (205, 184, 165)),
                                           (-10, -10, (205, 184, 165)),
                                           (10, 10, (219, 190, 192)),
                                           (100, 10, (97, 26, 58)),
                                           (78, 5, (211, 135, 139))
                                       ], 5)
        self.assertEqual(pos, (21, 21))
