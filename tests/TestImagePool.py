from pathlib import Path
from unittest import TestCase

from utils.ImagePoolUtils import ImagePool, NOTHING


class TestImagePool(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.home_path = Path("../")
        cls.work_path = Path("./")

    def test_nothing(self):
        print(NOTHING)
        item = NOTHING.a.b.b.e.f["as"].get(5)
        print(item)
        self.assertFalse(item is None)  # 不要使用 is
        self.assertEqual(item, None)
        self.assertFalse(item == 5)  # 除None外不与任何值相等

    def test_pool_path(self):
        pool: ImagePool = ImagePool(self.home_path, self.work_path)
        print(f"home: {pool.home()}")
        print(f"cwd: {pool.cwd()}")

    def test_work_path_error(self):
        self.assertRaises(ValueError, ImagePool, self.home_path, Path("../../"))

    def test_image_pool_base(self):
        pool: ImagePool = ImagePool(self.home_path, self.work_path)
        print(pool)
        images = pool.get("images")
        print(images)
        # 测试多种方式获取图片
        image1 = images.get("target.jpg")
        image2 = pool["images/target.jpg"]
        image3 = pool["images"]["target.jpg"]
        self.assertTrue(image1 is image2 is image3)

    def test_image_pool_more(self):
        # 缓存目录,每次获取相同
        pool = ImagePool(self.home_path, self.work_path)
        images1 = pool.get("images")
        images2 = pool["images"]
        self.assertTrue(images1 is images2)
        # 不缓存目录，每次获取不相同
        pool = ImagePool(self.home_path, self.work_path, cache_sub_pool=False)
        images1 = pool.get("images")
        images2 = pool["images"]
        self.assertFalse(images1 is images2)

    def test_get_none_error(self):
        pool = ImagePool(self.home_path)
        self.assertRaises(ValueError, pool.get, None)

    def test_scan(self):
        pool = ImagePool(self.home_path, self.work_path, scan=True)
        images = pool["images"]
        print(images)
        print(images.images)

    def test_ignore_suffix(self):
        pool = ImagePool(self.home_path, "tests/images", ignore_suffix=True)
        image1 = pool["target.jpg"]
        image2 = pool.target
        self.assertTrue(image1 is image2)

    def test_strict_model(self):
        pool = ImagePool(self.home_path, "tests/images", strict=True)
        pool.get("target.jpg")
        self.assertRaises(FileNotFoundError, pool.get, "target0.jpg")
