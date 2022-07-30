# textColor

### 简介
textColor 使用 [ANSI](https://zh.wikipedia.org/wiki/ANSI转义序列) 实现，用于打印具有样式的文本。

不同 Terminal 对 ANSI 的兼容性不同，使用前最好进行测试。

### 使用

#### 文本

文本使用 `Text` 对象来进行，可以设置模式、前景色、背景色。支持的选项分别在 ansi 中的Model、Color、BackColor中。

#### 光标

光标使用 `Cursor` 对象来进行，可以实现移动/保存/恢复光标位置、清空打印内容等操作。

### 实例

#### 文本

##### 模式

~~~python
from utils.textColor import Text, Model

print(Text("test").model(Model.ITALIC))
~~~

##### 模式叠加

~~~python
from utils.textColor import Text, Model

print(Text("test").model(Model.ITALIC).model(Model.UNDERSCORE)) # 并不是所有模式都可以叠加使用
~~~

##### 前景色

~~~python
from utils.textColor import Text, Color

print(Text("test").color(Color.YELLOW)) # 前景色还可以通过 color_256、color_rgb 来进行设置
~~~

##### 背景色

~~~python
from utils.textColor import Text, BackColor

print("test")
print(Text("test").bg(BackColor.BLUE)) # 背景色还可以通过 bg_256、bg_rgb 来进行设置
~~~

##### 混合使用

~~~python
from utils.textColor import Text, Model, Color, BackColor

print(Text("test").model(Model.OVERLINE).color(Color.GREEN).bg(BackColor.LIGHT_RED))
~~~

##### 嵌套使用

~~~python
from utils.textColor import Text, Model, Color, BackColor

t0 = Text("测试文字嵌套").color(Color.RED)
t1 = Text(f"测试文字嵌套1[{t0}]1测试文字嵌套1").bg(BackColor.LIGHT_RED)
t2 = Text(f"测试文字嵌套2[{t1}]测试文字嵌套2").color(Color.BLUE)
t3 = Text(f"测试文字嵌套3[{t2}]测试文字嵌套3").color(Color.LIGHT_YELLOW).model(Model.DOUBLE_UNDERSCORE)
print(t3)
~~~

#### 光标

##### 移动光标

```python
from utils.textColor import Cursor

for i in range(10):
    print(i)
print(Cursor.Save(), end="")
print(Cursor.Up(), end="")
print("edit 1", end="")
print(Cursor.Up(2), end="")
print("edit 2", end="")
print(Cursor.Restore(), end="")
```

##### 清除屏幕内容

~~~python
from utils.textColor import Cursor

for i in range(10):
    print(i)
print(Cursor.Up(5), end="")
print(Cursor.Erase_Display())
~~~

##### 获取光标位置

~~~python
from utils.textColor import Cursor


def get_ansi_device_status():
    import msvcrt
    s = msvcrt.getch()
    if s == b'\x1b':
        while True:
            t = msvcrt.getch()
            if t == b'R':
                break
            s += t
    return tuple(int(n) for n in s.split(b"[")[1].split(b";"))


for i in range(10):
    print(i)
print(Cursor.Device_Status())
print(get_ansi_device_status())
~~~

