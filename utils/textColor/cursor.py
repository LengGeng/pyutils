from .ansi import CSI


class Cursor:
    @staticmethod
    def Up(n: int = 1):
        """
        光标向上移动 n 行
        :param n: 行数
        :return:
        """
        return f"{CSI}{n}A"

    @staticmethod
    def Down(n: int = 1):
        """
        光标向上移动 n 行
        :param n: 行数
        :return:
        """
        return f"{CSI}{n}B"

    @staticmethod
    def Forward(n: int = 1):
        """
        光标向前(右)移动 n 列
        :param n: 列数
        :return:
        """
        return f"{CSI}{n}C"

    @staticmethod
    def Back(n: int = 1):
        """
        光标向后(左)移动 n 列
        :param n: 列数
        :return:
        """
        return f"{CSI}{n}D"

    @staticmethod
    def Next_Line(n: int = 1):
        """
        光标向下移动 n 行，并移动到行首
        :param n: 行数
        :return:
        """
        return f"{CSI}{n}E"

    @staticmethod
    def Previous_Line(n: int = 1):
        """
        光标向上移动 n 行，并移动到行首
        :param n: 行数
        :return:
        """
        return f"{CSI}{n}F"

    @staticmethod
    def Horizontal_Absolute(n: int = 1):
        """
        光标移动到第 n 列
        :param n:
        :return:
        """
        return f"{CSI}{n}F"

    @staticmethod
    def POS(x: int = 1, y: int = 1):
        """
        光标移动到 (x,y) 处
        :param x: 横坐标
        :param y: 列坐标
        :return:
        """
        return f"{CSI}{x};{y}H"

    @staticmethod
    def Erase_Display(m: int = 0):
        """
        清除屏幕的部分区域
        0: 清除从光标位置到屏幕末尾的部分
        1: 清除从光标位置到屏幕开头的部分
        2: 清除整个屏幕，光标向左上方移动
        3，清除整个屏幕，并删除回滚缓存区中的所有行
        :param m: 清除模式
        :return:
        """
        return f"{CSI}{m}J"

    @staticmethod
    def Erase_Line(m: int = 0):
        """
        清除行内的部分区域
        0: 清除从光标位置到该行末尾的部分
        1: 清除从光标位置到该行开头的部分
        2: 清除整行。光标位置不变
        :param m: 清除模式
        :return:
        """
        return f"{CSI}{m}K"

    @staticmethod
    def Scroll_Up(n: int = 1):
        """
        整页向上滚动 n 行，新行添加到底部
        :param n: 行数
        :return:
        """
        return f"{CSI}{n}S"

    @staticmethod
    def Scroll_Down(n: int = 1):
        """
        整页向下滚动 n 行，新行添加到顶部
        :param n: 行数
        :return:
        """
        return f"{CSI}{n}T"

    @staticmethod
    def Open_Auxiliary_Port():
        return f"{CSI}5i"

    @staticmethod
    def Close_Auxiliary_Port():
        return f"{CSI}4i"

    @staticmethod
    def Device_Status():
        """
        向应用程序报告光标位置
        :return:
        """
        return f"{CSI}6n"

    @staticmethod
    def Save():
        """
        保存光标的当前位置
        :return:
        """
        return f"{CSI}s"

    @staticmethod
    def Restore():
        """
        恢复保存的光标位置
        :return:
        """
        return f"{CSI}u"
