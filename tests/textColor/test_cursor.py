from utils.textColor.cursor import Cursor


def test_cursor_up():
    for i in range(10):
        print(i)
    print(Cursor.Up(), end="")
    print("edit 1", end="")
    print(Cursor.Up(2), end="")
    print("edit 2", end="")

    print("\n" * 5)


def test_cursor_down():
    for i in range(10):
        print(i)
    print(Cursor.Up(7), end="")
    print("up 1 edit", end="")
    print(Cursor.Down(3), end="")
    print("up 2 edit", end="")

    print("\n" * 5)


def test_cursor_forward():
    for i in range(10):
        print(i)
    print(Cursor.Up(7), end="")
    print("up 1 edit", end="")
    print(Cursor.Down(), end="")
    print(Cursor.Forward(5), end="")
    print("up 2 edit", end="")

    print("\n" * 5)


def test_cursor_back():
    for i in range(10):
        print(i)
    print(Cursor.Up(7), end="")
    print("up 1 edit", end="")
    print(Cursor.Down(), end="")
    print(Cursor.Back(8), end="")
    print("up 2 edit", end="")

    print("\n" * 5)


def test_cursor_pos():
    for _ in range(10):
        print('*' * 10)
    for i in range(10):
        print(Cursor.POS(i + 1, i + 1), end="")
        print(i + 1, end="")

    print("\n" * 5)


def escape_chars_encode(content: str):
    return str(content.encode()).removeprefix('b').strip("'")


def get_ansi_device_status():
    import msvcrt
    s = msvcrt.getch()
    if s == b'\x1b':
        while True:
            t = msvcrt.getch()
            if t == b'R':
                break
            s += t
    return tuple(int(i) for i in s.split(b"[")[1].split(b";"))


def test_cursor_save():
    print(Cursor.Save())
    for i in range(0):
        print(i)

    print(Cursor.Restore())
    print("123")


def test_cursor_device_status():
    print(Cursor.Device_Status())
    print(escape_chars_encode(Cursor.Device_Status()))
    print(get_ansi_device_status())


def test():
    test_cursor_up()
    print("*" * 50)
    test_cursor_down()
    print("*" * 50)
    test_cursor_forward()
    print("*" * 50)
    test_cursor_back()
    print("*" * 50)
    test_cursor_pos()
    print("*" * 50)
    test_cursor_save()


if __name__ == '__main__':
    test()
