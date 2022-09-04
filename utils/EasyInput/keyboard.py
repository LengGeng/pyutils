import msvcrt
from collections import namedtuple
from enum import Enum


class Key(Enum):
    # 方向键
    Up = '\xe0H'
    Left = '\xe0K'
    Down = "\xe0P"
    Right = "\xe0M"
    Delete = "\xe0S"
    # Fn 键
    F1 = "\x00;"
    F2 = "\x00<"
    F3 = "\x00="
    F4 = "\x00>"
    F5 = "\x00?"
    F6 = "\x00@"
    F7 = "\x00A"
    F8 = "\x00B"
    F9 = "\x00C"
    F10 = "\x00D"
    F11 = "\xe0\x85"
    F12 = "\xe0\x86"
    # 其他功能键
    Esc = "\x1b"
    Enter = "\r"
    Space = " "
    Tab = "\t"
    Backspace = "\x08"
    # 数字
    Number_0 = '0'
    Number_1 = '1'
    Number_2 = '2'
    Number_3 = '3'
    Number_4 = '4'
    Number_5 = '5'
    Number_6 = '6'
    Number_7 = '7'
    Number_8 = '8'
    Number_9 = '9'
    # 小写字母
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'
    g = 'g'
    h = 'h'
    i = 'i'
    j = 'j'
    k = 'k'
    l = 'l'
    m = 'm'
    n = 'n'
    o = 'o'
    p = 'p'
    q = 'q'
    r = 'r'
    s = 's'
    t = 't'
    u = 'u'
    v = 'v'
    w = 'w'
    x = 'x'
    y = 'y'
    z = 'z'
    # 大写字母
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    U = 'U'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'


Event = namedtuple("Event", ["key", "value"])


def listener(callback):
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getwch()
            if key in '\x00\xe0':  # arrow or function key prefix?
                key += msvcrt.getwch()  # second call returns the scan code
            # 创建 Event
            if key in Key._value2member_map_:
                k = Key(key)
                e = Event(key=k.name, value=k.value)
            else:
                e = Event(key=None, value=key)
            # 调用回调并判断返回值，返回值为 Key.Esc 退出
            if callback(e) == Key.Esc:
                break


def test():
    listener(lambda e: print(e))


if __name__ == '__main__':
    test()
