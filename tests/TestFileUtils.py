from unittest import TestCase

from utils import FileUtils


class TestFileUtils(TestCase):
    def test_check_dir(self):
        FileUtils.check_dirs("test_dir", "测试目录")

    def test_init_file(self):
        FileUtils.init_file("data.tmp", 1024 * 1024 * 128)

    def test_size_format(self):
        self.assertEqual(FileUtils.size_format(1024 * 1024 * 768), "768.0MB")
        self.assertEqual(FileUtils.size_format(1048576), "1.0MB")

    def test_replace_invalid_filename_char(self):
        filename = FileUtils.replace_invalid_filename_char('test"data*a.txt')
        self.assertEqual(filename, "test_data_a.txt")
