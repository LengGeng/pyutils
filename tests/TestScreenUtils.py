from unittest import TestCase

from utils import ScreenUtils


class TestScreenUtils(TestCase):
    def test_get_screensize(self):
        print(ScreenUtils.get_screensize())

    def test_adapt_scaling(self):
        scaling = ScreenUtils.adapt_scaling((250, 500), (900, 600))
        self.assertEqual(scaling, (300.0, 600.0))

    def test_suitable_screensize(self):
        screensize = ScreenUtils.suitable_screensize((1920, 1080))
        self.assertEqual(screensize, screensize)
