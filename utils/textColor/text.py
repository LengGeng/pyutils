from .ansi import Model, Color, BackColor, CSI

RESET = f"{CSI}0m"


class Text:
    def __init__(self, text: str = ""):
        self._text = text
        self._models = [Model.DEFAULT.value]
        self._color = Color.DEFAULT.value
        self._bg_color = BackColor.DEFAULT.value

    def text(self, text: str):
        """
        重新设置字体
        :param text:
        :return:
        """
        self._text = text
        return self

    def render(self, text: str):
        """
        使用样式渲染文本,原有文本不会改变
        :param text: 渲染的文本内容
        :return:
        """
        _old = self._text
        self._text = text
        print(self)
        self._text = _old

    def model(self, model: Model):
        """
        设置模式
        :param model: 模式代码
        :return:
        """
        # 判断是否是清除
        if model.value == Model.DEFAULT:
            self._models.clear()
        # 判断当前模式代码是否存在，存在需要放至最后
        if model.value in self._models:
            self._models.remove(model.value)
        # 添加模式代码
        self._models.append(model.value)
        return self

    def color(self, color: Color):
        """
        设置字体颜色
        :param color: 字体颜色代码
        :return:
        """
        self._color = color.value
        return self

    def color_256(self, color: int):
        """
        通过 256 色代码设置字体颜色
        颜色参照表: https://zh.wikipedia.org/wiki/ANSI转义序列#8位
        :param color: 颜色代码 0-255
        :return:
        """
        self._color = f"38;5;{color}"
        return self

    def color_rgb(self, r: int, g: int, b: int):
        """
        通过 rgb 设置字体颜色
        :param r: 红 0-255
        :param g: 绿 0-255
        :param b: 蓝 0-255
        :return:
        """
        self._color = f"38;2;{r};{g};{b}"
        return self

    def bg(self, color: BackColor):
        """
        设置背景色
        :param color: 背景色代码
        :return:
        """
        self._bg_color = color.value
        return self

    def bg_256(self, color: int):
        """
        通过 256 色代码设置背景颜色
        颜色参照表: https://zh.wikipedia.org/wiki/ANSI转义序列#8位
        :param color: 颜色代码 0-255
        :return:
        """
        self._bg_color = f"48;5;{color}"
        return self

    def bg_rgb(self, r: int, g: int, b: int):
        """
        通过 rgb 设置背景颜色
        :param r: 红 0-255
        :param g: 绿 0-255
        :param b: 蓝 0-255
        :return:
        """
        self._bg_color = f"48;2;{r};{g};{b}"
        return self

    @property
    def _model(self):
        """
        合并模式代码
        :return:
        """
        return ';'.join([str(code) for code in self._models])

    @property
    def style(self):
        """
        合并样式代码
        :return:
        """
        return f"{CSI}{self._model};{self._color};{self._bg_color}m"

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        content = self.style + str(self._text) + RESET
        return content.replace(RESET, self.style) + RESET
