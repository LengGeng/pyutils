# pyutils

### 简介

收集整理了一些在项目中经常使用的代码片段(函数/类/模块等)。

### 列表

#### [textColor](utils/textColor)

> textColor 使用 [ANSI](https://zh.wikipedia.org/wiki/ANSI转义序列) 实现，用于打印具有样式的文本。
>
> 不同 Terminal 对 ANSI 的兼容性不同，使用前最好进行测试。

#### [EasyInput](utils/EasyInput)

依赖: `textColor`

> EasyInput 是一个可以提供更好交互的输入工具。
>
> 提供了多种交互的输入方式(文本、密码、数字、确认、单选、多选)。
>
> 由于依赖 `textColor` 因此兼容性略差，使用前最好进行测试。

#### [PosUtils](utils/PosUtils.py)

> PosUtils 是一个表示位置坐标的工具，提供了点(Pos)、范围(Scope)等。