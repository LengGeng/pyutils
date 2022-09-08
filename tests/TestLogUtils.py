from unittest import TestCase

from utils import LogUtils


class TestLogUtils(TestCase):
    logger = None

    def test_default_logger(self):
        self.logger = LogUtils.LogUtils(__name__).getLogger()

    def test_file_handler(self):
        self.logger = LogUtils.LogUtils(__name__, filename="test.log").getLogger()

    def test_level(self):
        self.logger = LogUtils.LogUtils(__name__, LogUtils.ERROR).getLogger()

    def test_respectively_level(self):
        self.logger = LogUtils.LogUtils(__name__, LogUtils.DEBUG, default_handler=False). \
            add_sh_handler(LogUtils.INFO). \
            add_file_handler("test.log", LogUtils.DEBUG).getLogger()

    def tearDown(self) -> None:
        self.logger.debug("debug log ...")
        self.logger.info("info log ...")
        self.logger.warning("warning log ...")
        self.logger.error("error log ...")
