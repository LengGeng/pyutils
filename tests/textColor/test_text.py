from utils.textColor import Text
from utils.textColor import Model, Color, BackColor
from code_desc import CODE_DESC

render = Text().color_256(208).bg_256(0).model(Model.FRAMED)


def test_model_all():
    render.render("测试所有模式")
    for model in Model:
        text = Text(f"测试模式[{model.value}]-{CODE_DESC[model.value]}")
        text.model(model)
        print(text)


def test_model_overlay():
    render.render("测试模式叠加")
    text = Text("测试模式")
    for model in Model:
        text._text = f"[{model.value}]-{CODE_DESC[model.value]}"
        text.model(model)
        print(text)


def test_model_remove():
    render.render("模式取消测试")
    # 测试取消斜体-O
    print("\033[3m 测试取消斜体 \033[0m")
    print("\033[3;23m 测试取消斜体 \033[0m")
    # 测试取消尖角体-?
    print("\033[20m 测试取消尖角体 \033[0m")
    print("\033[20;23m 测试取消尖角体 \033[0m")
    # 测试取消下划线-OK
    print("\033[4m 测试取消下划线 \033[0m")
    print("\033[4;24m 测试取消下划线 \033[0m")
    print("\033[21m 测试取消双下划线 \033[0m")
    print("\033[21;24m 测试取消双下划线 \033[0m")
    # 测试取消反显-OK
    print("\033[7m 测试取消反显 \033[0m")
    print("\033[7;27m 测试取消反显 \033[0m")
    # 测试取消删除线-OK
    print("\033[9m 测试取消删除线 \033[0m")
    print("\033[9;29m 测试取消删除线 \033[0m")


def test_color_all():
    render.render("测试所有颜色")
    text = Text("测试颜色")
    bg_text = Text("测试背景颜色")
    for color, bg in zip(Color, BackColor):
        text._text = f"前景色[{color.value}]-{CODE_DESC[color.value]}"
        bg_text._text = f"背景色[{bg.value}]-{CODE_DESC[bg.value]}"
        text.color(color)
        bg_text.bg(bg)
        print(text, '\t', bg_text)


def test_color_256():
    render.render("测试通过颜色表数值设置颜色")
    color = 155
    bgColor = 212
    text = Text(f"RGB Color Color:{color},bgColor:{bgColor}").color_256(color).bg_256(bgColor)
    print(text)


def test_color_rgb():
    render.render("测试通过 RGB 设置颜色")
    color = (155, 200, 156)
    bgColor = (25, 156, 255)
    text = Text(f"RGB Color Color:{color},bgColor:{bgColor}").color_rgb(*color).bg_rgb(*bgColor)
    print(text)


def test_nested():
    render.render("测试嵌套文字")
    t0 = Text("测试文字嵌套").color(Color.RED)
    t1 = Text(f"测试文字嵌套1[{t0}]1测试文字嵌套1").bg(BackColor.LIGHT_RED)
    t2 = Text(f"测试文字嵌套2[{t1}]测试文字嵌套2").color(Color.BLUE)
    t3 = Text(f"测试文字嵌套3[{t2}]测试文字嵌套3").color(Color.LIGHT_YELLOW).model(Model.DOUBLE_UNDERSCORE)
    print(t3)


def test_border():
    render.render("测试边框")
    print("\033[51m 测试 \033[0m")
    print()
    print("\033[52m 测试 \033[0m")
    print()
    print("\033[51;54m 测试 \033[0m")
    print("\033[52;54m 测试 \033[0m")


def test_other():
    render.render("兼容性较差的测试")
    print("\033[60m 测试 \033[0m")
    print("\033[61m 测试 \033[0m")
    print("\033[62m 测试 \033[0m")
    print("\033[63m 测试 \033[0m")
    print("\033[64m 测试 \033[0m")
    print("\033[65m 测试 \033[0m")


def test():
    test_model_all()
    test_model_overlay()
    test_model_remove()
    test_color_all()
    test_color_256()
    test_color_rgb()
    test_nested()
    test_border()
    test_other()


if __name__ == '__main__':
    test()
