from PySide6.QtGui import QIcon
from enum import Enum


class State(Enum):
    NORMAL = 10
    PRESS = 20
    HOVER = 30
    SELECT = 40



class StateIcon:
    def __init__(self):
        self.normal: QIcon = QIcon()
        self.press: QIcon = QIcon()
        self.hover: QIcon = QIcon()
        self.select: QIcon = QIcon()