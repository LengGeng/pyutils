from collections import namedtuple
from typing import Optional, Union, List
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from .keyboard import listener, Event, Key
from utils.textColor import Text, Color, Cursor, Model

# 定义常见允许输入的值 (大小写字母+数字)
ACCEPT = ascii_lowercase + ascii_uppercase + digits

# 定义几种常用的样式渲染器
questionRender = Text().color(Color.GREEN)
defaultRender = Text().color(Color.BLUE)
resultRender = Text().color(Color.YELLOW)
markRender = Text().model(Model.HIGHLIGHT).color(Color.GREEN)

# 定义几种常用符号
Q = str(questionRender.text('?'))
A = str(resultRender.text('√'))
ITEM = str(questionRender.text('❯'))
SELECT = '○'
SELECTED = '●'


class RangeNumber:

    def __init__(self, s: int, e: Optional[int] = None):
        if e is None:
            self.s = 1
            self.e = s
        else:
            self.s = s
            self.e = e
        assert self.e > self.s
        self.count = self.e - self.s + 1
        self.value = self.s

    def set(self, num: int):
        self.value = num

    def add(self, num: int = 1):
        if num < 0:
            self.sub(num * -1)
        num = num % self.count
        self.value += num
        if self.value > self.e:
            self.value -= self.count

    def sub(self, num: int = 1):
        if num < 0:
            self.add(num * -1)
        num = num % self.count
        self.value -= num
        if self.value < self.s:
            self.value += self.count

    def __repr__(self):
        return f"RangeNumber({self.value}>{{{self.s},{self.e}}})"


class Input:
    def __init__(self, title: str, default=None):
        self.title = title
        self.default = default
        self.content: str = ""  # 保存用户输入的内容
        # 保存运行前的光标位置
        self._save_cursor_()

    @staticmethod
    def _save_cursor_():
        """
        保存运行前的光标位置
        :return:
        """
        print(Cursor.Save(), end="")

    @staticmethod
    def _restore_cursor_():
        """
        恢复光标到运行前的位置，并清空自身打印的字符
        :return:
        """
        print(Cursor.Restore(), end="")
        print(Cursor.Erase_Display(), end="")

    def get(self):
        self.handle_prompt()
        self.handle_input()
        return self.handle_result()

    def handle_prompt(self):
        """处理问题
        处理信息并进行提问
        :return:
        """
        pass

    def handle_input(self):
        """处理用户输入
        根据用户输入进行交互
        :return:
        """
        pass

    def handle_result(self):
        """返回处理结果
        处理并返回、展示输入结果
        :return:
        """
        pass


class String(Input):
    """
    提供文本输入交互
    """

    def __init__(self, title, default=""):
        super(String, self).__init__(title, default)

    def handle_prompt(self):
        self._restore_cursor_()
        if self.content:
            value = resultRender.text(self.content)
        else:
            value = "" if self.default is None or self.default == "" else f"({defaultRender.text(self.default)})"
        question = f"[{Q}] {self.title} {value}"
        print(question, end="", flush=True)

    def _handle_input_(self, event: Event):
        # 处理已知输入
        if event.key:
            # 回车终止输入
            if event.key == Key.Enter.name:
                return Key.Esc
            # 删除键删除已有内容
            elif event.key == Key.Backspace.name:
                self.content = self.content[:-1]
            # 处理输入数字和字母
            if event.value in ACCEPT:
                self.content += event.value
        # 处理其它输入
        else:
            # 符号和其它文字
            self.content += event.value
        # 刷新显示
        self.handle_prompt()

    def handle_input(self):
        listener(self._handle_input_)

    def handle_result(self):
        # 清空交互过程中产生的打印
        self._restore_cursor_()
        # 处理结果
        result = self.content or self.default
        # 输出结果
        print(f"[{A}] {self.title} {resultRender.text(result)}")
        # 返回结果
        return result


class Password(Input):
    """提供密码输入交互"""

    def __init__(self, title):
        super(Password, self).__init__(title, default="")

    def handle_prompt(self):
        self._restore_cursor_()
        value = '*' * len(self.content)
        question = f"[{Q}] {self.title} {value}"
        print(question, end="", flush=True)

    def _handle_input_(self, event: Event):
        # 处理已知输入
        if event.key:
            # 回车终止输入
            if event.key == Key.Enter.name:
                return Key.Esc
            # 删除键删除已有内容
            elif event.key == Key.Backspace.name:
                self.content = self.content[:-1]
            # 处理输入数字和字母
            if event.value in ACCEPT:
                self.content += event.value
        # 处理其它输入
        else:
            # 符号
            if event.value in punctuation:
                self.content += event.value
        self.handle_prompt()

    def handle_input(self):
        listener(self._handle_input_)

    def handle_result(self) -> str:
        # 清空交互过程中产生的打印
        self._restore_cursor_()
        # 处理结果
        result = self.content
        # 输出结果
        print(f"[{A}] {self.title} {'*' * len(self.content)}")
        # 返回结果
        return result


class Number(Input):
    """
    提供数字输入交互
    """

    def __init__(self, title, default=0):
        super(Number, self).__init__(title, default)

    def handle_prompt(self):
        self._restore_cursor_()
        if self.content:
            value = resultRender.text(self.content)
        else:
            value = "" if self.default is None else f"({defaultRender.text(self.default)})"
        question = f"[{Q}] {self.title} {value}"
        print(question, end="", flush=True)

    def _handle_input_(self, event: Event):
        # 处理已知输入
        if event.key:
            # 回车终止输入
            if event.key == Key.Enter.name:
                return Key.Esc
            # 删除键删除已有内容
            elif event.key == Key.Backspace.name:
                self.content = self.content[:-1]
            # 处理输入数字
            if event.value in digits:
                self.content += event.value
        # 处理其它输入
        else:
            # 处理输入小数点
            if event.value == '.':
                # 内容中只会出现一次 '.'
                if '.' not in self.content:
                    self.content += event.value
        self.handle_prompt()

    def handle_input(self):
        listener(self._handle_input_)

    def handle_result(self):
        # 清空交互过程中产生的打印
        self._restore_cursor_()
        # 处理结果
        if self.content:
            # 去除末尾无用的 '.'
            self.content: str = self.content.rstrip(".")
            if '.' in self.content:
                # 判断首位为 '.'
                if self.content[0] == '.':
                    self.content = '0' + self.content
                result = float(self.content)
            else:
                result = int(self.content)
        else:
            result = self.default
        # 输出结果
        print(f"[{A}] {self.title} {resultRender.text(result)}")
        # 返回结果
        return result


class Confirm(Input):
    """
    提供是否输入交互
    """

    def __init__(self, title, default=True):
        super(Confirm, self).__init__(title, default)

    def handle_prompt(self):
        self._restore_cursor_()
        if self.content:
            value = resultRender.text(self.content)
        else:
            if self.default:
                value = f"({defaultRender.text('Y')}/N) 【输入y,n进行选择,或使用Tab进行切换】"
            else:
                value = f"(Y/{defaultRender.text('N')})"

        question = f"[{Q}] {self.title} {value}"
        print(question, end="", flush=True)

    def _handle_input_(self, event: Event):
        # 处理已知输入
        if event.key:
            # 回车终止输入
            if event.key == Key.Enter.name:
                return Key.Esc
            # 删除键删除已有内容
            elif event.key == Key.Backspace.name:
                self.content = self.content[:-1]
            # 处理 Tab 键切换
            elif event.key == Key.Tab.name:
                # Tab 取反
                self.content = "N" if self.result else "Y"
            # 处理输入 Y N
            if event.value.upper() in "YN":
                self.content = event.value.upper()
        self.handle_prompt()

    def handle_input(self):
        listener(self._handle_input_)

    def handle_result(self) -> bool:
        # 清空交互过程中产生的打印
        self._restore_cursor_()
        # 处理结果
        result = "Y" if self.result else "N"
        # 打印结果
        print(f"[{A}] {self.title} {resultRender.text(result)}")
        # 返回结果
        return self.result

    @property
    def result(self) -> bool:
        if self.content:
            return self.content == "Y"
        else:
            return self.default


Option = namedtuple("Option", ["title", "value", "selected"])


def parseOption(opts: Union[list, dict]) -> List[Option]:
    options: List[Option] = []
    if isinstance(opts, dict):
        for k, v in opts.items():
            option = Option(k, v, False)
            options.append(option)
    elif isinstance(opts, list):
        for opt in opts:
            if isinstance(opt, str):
                option = Option(opt, opt, False)
            elif isinstance(opt, dict):
                title = opt.get("title")
                value = opt.get("value")
                if value is None:
                    value = title
                selected = opt.get("selected")
                option = Option(title, value, selected)
            else:
                raise TypeError('options 应该是由 str 或 dict 组成的列表')
            options.append(option)
    else:
        raise Exception("options type error")
    return options


class Radio(Input):
    """
    提供单选7输入交互
    """

    def __init__(self, title: str, options: list, default: Union[str, int] = 0):
        super().__init__(title)
        # 处理选项
        self.options = parseOption(options)
        # print(self.options)
        # 处理默认值
        if isinstance(default, str):
            # 判断是否在数组中并获取下标
            self.default = 0
            for i, opt in enumerate(self.options):
                if opt.title == default:
                    self.default = i
                    break
        elif isinstance(default, int):
            # 判断下标是否越界
            if 0 <= default < len(self.options):
                self.default = default
            else:
                raise IndexError("默认值索引超出范围")
        else:
            self.default = 0
        # 选中索引
        self.index = RangeNumber(0, len(self.options) - 1)
        self.index.set(self.default)
        # 提示
        self.tips = "(上下键切换选项，回车确认选择)"
        self.show_tips = True

    def handle_prompt(self):
        self._restore_cursor_()
        if self.show_tips:
            value = defaultRender.text(self.tips)
        else:
            value = resultRender.text(self.options[self.index.value].title)
        question = f"[{Q}] {self.title} {value}"
        # 输出问题
        print(question)
        # 输出选项
        for i, option in enumerate(self.options):
            if i == self.index.value:
                print(markRender.text(f"  {i + 1}. {option.title}"))
            else:
                print(f"  {i + 1}. {option.title}")

    def _handle_input_(self, event: Event):
        # 处理已知输入
        if event.key:
            # 回车终止输入
            if event.key == Key.Enter.name:
                return Key.Esc
            # 上键
            elif event.key == Key.Up.name:
                self.index.sub()
                self.show_tips = False
            # 下键
            elif event.key == Key.Down.name:
                self.index.add()
                self.show_tips = False
        self.handle_prompt()

    def handle_input(self):
        listener(self._handle_input_)

    def handle_result(self):
        # 清空交互过程中产生的打印
        self._restore_cursor_()
        # 处理结果
        result = self.options[self.index.value].value
        # 打印结果
        print(f"[{A}] {self.title} {resultRender.text(result)}")
        # 返回结果
        return result


class Checkbox(Input):
    """
    提供多选输入交互
    """

    def __init__(self, title: str, options: list, defaults: Optional[List[bool]] = None):
        super().__init__(title)
        # 处理选项
        self.options = parseOption(options)
        # 处理默认值
        if defaults:
            if len(defaults) > len(self.options):
                raise TypeError("默认值比字段名称更多")
            for i, default in enumerate(defaults):
                self.options[i].selected = default
        # 选中索引
        self.index = RangeNumber(0, len(self.options) - 1)
        # 提示
        self.tips = "(上下键切换选项，空格进行选中，回车确认选择)"
        self.show_tips = True

    def handle_prompt(self):
        self._restore_cursor_()
        if self.show_tips:
            value = defaultRender.text(self.tips)
        else:
            value = resultRender.text(self.selected)
        question = f"[{Q}] {self.title} {value}"
        # 输出问题
        print(question)
        # 输出选项
        for i, option in enumerate(self.options):
            symbol = SELECTED if option.selected else SELECT
            if i == self.index.value:
                print(markRender.text(f"  {symbol}  {option.title}"))
            else:
                print(f"  {symbol}  {option.title}")

    def _handle_input_(self, event: Event):
        # 处理已知输入
        if event.key:
            # 回车终止输入
            if event.key == Key.Enter.name:
                return Key.Esc
            # 上键
            elif event.key == Key.Up.name:
                self.index.sub()
                self.show_tips = False
            # 下键
            elif event.key == Key.Down.name:
                self.index.add()
                self.show_tips = False
            # 空格选中
            elif event.key == Key.Space.name:
                self.show_tips = False
                option = self.options[self.index.value]
                self.options[self.index.value] = option._replace(selected=not option.selected)
        self.handle_prompt()

    def handle_input(self):
        listener(self._handle_input_)

    def handle_result(self):
        # 清空交互过程中产生的打印
        self._restore_cursor_()
        # 处理结果
        result = self.selected
        # 打印结果
        print(f"[{A}] {self.title} {resultRender.text(result)}")
        # 返回结果
        return result

    @property
    def selected(self):
        return [opt.value for opt in self.options if opt.selected]
