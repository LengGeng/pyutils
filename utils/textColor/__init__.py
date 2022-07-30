import os

from .text import Text
from .ansi import Model, Color, BackColor
from .cursor import Cursor

# Windows兼容
if os.name == "nt":
    os.system("")
