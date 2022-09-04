# EasyInput

### 简介

EasyInput 是一个可以提供更好交互的输入工具。

提供了多种交互的输入方式(文本、密码、数字、确认、单选、多选)。

由于依赖 `textColor` 因此兼容性略差，使用前最好进行测试。

### 使用

#### 文本(String)

~~~python
name = String("请输入姓名: ", "张三").get()
print(name)
~~~

#### 密码(Password)

~~~python
password = Password("请输入密码: ").get()
print(password)
~~~

#### 数字(Number)

~~~python
age = Number("请输入年龄: ", 16).get()
print(age)
~~~

#### 确认(Confirm)

~~~python
confirm = Confirm("是否接受用户协议: ").get()
print(confirm)
~~~

#### 单选(Radio)

~~~python
difficulty = Radio("选择难度: ", default="普通", options=["简单", "普通", "困难", "地狱"]).get()
print(difficulty)
~~~

#### 多选(Checkbox)

~~~python
hobby = Checkbox("你的爱好: ", options=["唱", "跳", "Rap", "篮球"]).get()
print(hobby)
~~~

#### 选项参数(单选、多选)

单选、多选的 `options` 参数使用方式相同。都有如下三个选项

- `title`: 选项显示的标题
- `value`: 选项实际代表的值
- `selected`: 是否选中(单选中该项无效)

例如上面的多选中的例子，它的 `options` 也可以写成这样

~~~python
options = [
    {
        "title": "唱",
        "value": "Sing",
        "selected": True
    },
    {
        "title": "跳",
        "value": "Jump"
    },
    {
        "title": "Rap",
        "value": "Rap",
        "selected": True
    },
    {
        "title": "篮球",
        "value": "Basketball"
    }
]
~~~

当不需要对是否选中进行设置时，可以简写成 `title:value` 的形式。

~~~python
options = {
    "唱": "Sing",
    "跳": "Jump",
    "Rap": "Rap",
    "篮球": "Basketball"
}
~~~

当 `title` 和 `value` 的值相同时，还可以再简写。

~~~python
options = ["唱", "跳", "Rap", "篮球"]
~~~

### 配置项写法

除了上述的使用函数调用式的写法，还可以使用配置项写法。

通过传入配置项进行解析依次调用，并返回答案对象。

其中问题的 `name` 参数表示该项答案在答案字典中的 `key`。

~~~python
from utils.EasyInput import prompt

questions = [
    {
        "name": "name",
        "type": "string",
        "title": "请输入姓名: ",
        "default": "张三"
    },
    {
        "name": "age",
        "type": "number",
        "title": "请输入年龄: ",
        "default": 16
    },
    {
        "name": "password",
        "type": "password",
        "title": "请输入密码: "
    },
    {
        "name": "difficulty",
        "type": "radio",
        "title": "选择难度: ",
        "default": "普通",
        "options": ["简单", "普通", "困难", "地狱"],
    },
    {
        "name": "hobby",
        "type": "checkbox",
        "title": "你的爱好: ",
        "options": ["唱", "跳", "Rap", "篮球"]
    }
]

answers = prompt(questions)
print(answers)
# >>> {'name': 'zs', 'age': 22, 'password': '123456', 'difficulty': '困难', 'hobby': ['唱', '跳', 'Rap']}
~~~

