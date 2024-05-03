from PySide6.QtCore import QObject, Qt, Signal
from PySide6.QtGui import QColor

from typing import Self
from qbclient.Widgets.Icon.state import State




class IconColor:
    DEFAULT = QColor(Qt.GlobalColor.black)

    class __Signal(QObject):
        iconColorChanged = Signal(State)

    def __init__(self):
        self.__normal = IconColor.DEFAULT
        self.__press = IconColor.DEFAULT
        self.__hover = IconColor.DEFAULT
        self.__select = IconColor.DEFAULT

        self.__signal = IconColor.__Signal()
        self.iconColorChanged = self.__signal.iconColorChanged


    @property
    def normal(self) -> QColor:
        return self.__normal

    @property
    def press(self) -> QColor:
        return self.__press

    @property
    def hover(self) -> QColor:
        return self.__hover

    @property
    def select(self) -> QColor:
        return self.__select




    def setNormal(self, color: Qt.GlobalColor | QColor | str):
        self.__normal = self.__getQColor(color)
        self.iconColorChanged.emit(State.NORMAL)


    def setPress(self, color: Qt.GlobalColor | QColor | str):
        self.__press = self.__getQColor(color)
        self.iconColorChanged.emit(State.PRESS)


    def setHover(self, color: Qt.GlobalColor | QColor | str):
        self.__hover = self.__getQColor(color)
        self.iconColorChanged.emit(State.HOVER)


    def setSelect(self, color: Qt.GlobalColor | QColor | str):
        self.__select = self.__getQColor(color)
        self.iconColorChanged.emit(State.SELECT)




    def copy(self) -> Self:
        sc = IconColor()
        sc.normal = self.__normal
        sc.press = self.__press
        sc.hover = self.__hover
        sc.select = self.__select
        return sc




    def __getQColor(self, color: Qt.GlobalColor | QColor | str) -> QColor:
        if type(color) is QColor:
            return color
        else:
            return QColor(color)


