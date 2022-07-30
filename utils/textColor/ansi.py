from enum import Enum

# ref
# https://zh.wikipedia.org/wiki/ANSI转义序列
# http://en.wikipedia.org/wiki/ANSI_escape_code

CSI = "\033["


class Model(Enum):
    """模式"""
    DEFAULT = 0  # 默认样式（清除样式)
    HIGHLIGHT = 1  # 突出显示(加粗、高亮)
    DIM = 2  # 暗淡
    ITALIC = 3  # 斜体
    UNDERSCORE = 4  # 下划线
    FLICKER = 5  # 闪烁(慢)
    FLICKER_FAST = 6  # 闪烁(快)
    ANTI_WHITE = 7  # 反显
    HIDE = 8  # 隐藏
    ERASE = 9  # 划除(删除线)
    PRIMARY = 10  # 主要(默认)字体
    # 11-19 其它替代字体
    SHARP_CORNERS = 20  # 尖角体
    DOUBLE_UNDERSCORE = 21  # 双下划线

    HIGHLIGHT_RM = 22  # 去除突出显示 <1>
    ITALIC_RM = 23  # 去除斜体 <3>
    UNDERSCORE_RM = 24  # 去除下划线、双下划线 <4,21>
    FLICKER_RM = 25  # 关闭闪烁 <5,6>
    ANTI_WHITE_RM = 27  # 关闭反显 <7>
    HIDE_RM = 28  # 关闭隐藏 <8>
    ERASE_RM = 29  # 关闭删除线 <9>

    FRAMED = 51  # 凹陷边框
    ENCIRCLED = 52  # 包围边框
    OVERLINE = 53  # 上划线
    BORDER_RM = 54  # 取消边框
    OVERLINE_RM = 55  # 取消上划线


class Color(Enum):
    """文字颜色"""
    BLACK = 30  # 黑
    RED = 31  # 红
    GREEN = 32  # 绿
    YELLOW = 33  # 黄
    BLUE = 34  # 蓝
    MAGENTA = 35  # 品红(紫)
    CYAN = 36  # 青
    WHITE = 37  # 白
    DEFAULT = 39  # 默认

    LIGHT_BLACK = 90  # 亮黑(灰)
    LIGHT_RED = 91  # 亮红
    LIGHT_GREEN = 92  # 亮绿
    LIGHT_YELLOW = 93  # 亮黄
    LIGHT_BLUE = 94  # 亮蓝
    LIGHT_MAGENTA = 95  # 亮品红
    LIGHT_CYAN = 96  # 亮青
    LIGHT_WHITE = 97  # 亮白


class BackColor(Enum):
    """背景色"""
    BLACK = 40  # 黑
    RED = 41  # 红
    GREEN = 42  # 绿
    YELLOW = 43  # 黄
    BLUE = 44  # 蓝
    MAGENTA = 45  # 品红(紫)
    CYAN = 46  # 青
    WHITE = 47  # 白
    DEFAULT = 49  # 默认

    LIGHT_BLACK = 100  # 亮黑(灰)
    LIGHT_RED = 101  # 亮红
    LIGHT_GREEN = 102  # 亮绿
    LIGHT_YELLOW = 103  # 亮黄
    LIGHT_BLUE = 104  # 亮蓝
    LIGHT_MAGENTA = 105  # 亮品红
    LIGHT_CYAN = 106  # 亮青
    LIGHT_WHITE = 107  # 亮白
