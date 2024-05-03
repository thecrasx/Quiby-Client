from PySide6.QtGui import QEnterEvent, QMouseEvent, QPixmap, QIcon
from PySide6.QtWidgets import QPushButton, QWidget

from qbclient.Widgets.Icon.icon import Icon, IconColor, State




class Button(QPushButton):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.__icon = None
        self.__hovered = False




    def icon(self) -> Icon:
        return self.__icon

    def qIcon(self) -> QIcon:
        return super().icon()


    def setQIcon(self, icon: QIcon | QPixmap |str):
        super().setIcon(icon)


    def setIcon(self, path: str, icon_color: IconColor = None):
        if self.__icon is None:
            if icon_color is None: icon_color = IconColor()

            self.__icon = Icon(path, icon_color)
            self.__icon.iconColor().iconColorChanged.connect(self.__onIconColorChange)

        else:
            self.__icon.load(path, icon_color)

        super().setIcon(self.__icon.get())




    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)

        if self.__icon:
            self.setQIcon(self.__icon.get(State.PRESS))




    def mouseReleaseEvent(self, event: QMouseEvent):
        super().mouseReleaseEvent(event)

        if self.__icon:
            if self.__hovered:
                self.setQIcon(self.__icon.get(State.HOVER))
            else:
                self.setQIcon(self.__icon.get(State.NORMAL))




    def enterEvent(self, event: QEnterEvent):
        super().enterEvent(event)
        self.__hovered = True

        if self.__icon:
            self.setQIcon(self.__icon.get(State.HOVER))




    def leaveEvent(self, event: QEnterEvent):
        super().leaveEvent(event)
        self.__hovered = False

        if self.__icon:
            self.setQIcon(self.__icon.get(State.NORMAL))
    



    def __onIconColorChange(self, _):
        self.setQIcon(self.__icon.get())