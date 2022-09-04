from utils.EasyInput import prompt, String, Number, Password, Confirm, Radio, Checkbox


def test_base():
    name = String("请输入姓名: ", "张三").get()
    age = Number("请输入年龄: ", 16).get()
    password = Password("请输入密码: ").get()
    confirm = Confirm("是否接受用户协议: ").get()
    difficulty = Radio("选择难度: ", default="普通", options=["简单", "普通", "困难", "地狱"]).get()
    hobby = Checkbox("你的爱好: ", options=["唱", "跳", "Rap", "篮球"]).get()

    print("输入结果")
    print(f"姓名: {name}({type(name)})")
    print(f"年龄: {age}({type(age)})")
    print(f"密码: {password}({type(password)})")
    print(f"是否接受用户协议: {confirm}({type(confirm)})")
    print(f"难度: {difficulty}({type(difficulty)})")
    print(f"爱好: {hobby}({type(hobby)})")


def test_prompt():
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
        },
    ]
    answers = prompt(questions)
    print(answers)


def test_radio_options():
    questions = [
        # dict
        {
            "name": "radio_dict",
            "type": "radio",
            "title": "选择难度: ",
            "default": "普通",
            "options": {
                "简单": "simple",
                "普通": "ordinary",
                "困难": "difficulty",
                "地狱": "hell"
            }
        },
        # list[str]
        {
            "name": "radio_list_str",
            "type": "radio",
            "title": "选择难度: ",
            "default": "普通",
            "options": ["简单", "普通", "困难", "地狱"],
        },
        # list[dict]
        {
            "name": "radio_list_dict",
            "type": "radio",
            "title": "选择难度: ",
            "default": "普通",
            "options": [
                {
                    "title": "简单",
                    "value": "simple"
                },
                {
                    "title": "普通",
                    "value": "ordinary"
                },
                {
                    "title": "困难",
                    "value": "difficulty"
                },
                {
                    "title": "地狱",
                    "value": "hell"
                }
            ]
        },
    ]
    answers = prompt(questions)
    print(answers)


def test_checkbox_options():
    questions = [
        # dict
        {
            "name": "checkbox_dict",
            "type": "checkbox",
            "title": "你的爱好: ",
            "options": {
                "唱": "Sing",
                "跳": "Jump",
                "Rap": "Rap",
                "篮球": "Basketball"
            }
        },
        # list[str]
        {
            "name": "checkbox_list_str",
            "type": "checkbox",
            "title": "你的爱好: ",
            "options": ["唱", "跳", "Rap", "篮球"]
        },
        # list[dict]
        {
            "name": "checkbox_list_dict",
            "type": "checkbox",
            "title": "你的爱好: ",
            "options": [
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
                },
            ]
        },
    ]
    answers = prompt(questions)
    print(answers)


if __name__ == '__main__':
    test_base()
    test_prompt()
    test_radio_options()
    test_checkbox_options()
