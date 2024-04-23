from PySide6.QtGui import QEnterEvent, QMouseEvent, QPainter, QBrush, QPen
from PySide6.QtCore import QEvent, Qt, QLine
from PySide6.QtWidgets import QPushButton, QWidget





class ButtonColor:
    NORMAL = Qt.GlobalColor.darkGray
    HOVER = Qt.GlobalColor.white
    PRESSED = Qt.GlobalColor.black




class TitleBarButton(QPushButton):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.__btnColor = ButtonColor.NORMAL
        self.__isHovered = False
        self.__padding = 10


    def setPadding(self, padding: int):
        self.__padding = padding
        self.update()



    def getPadding(self) -> int:
        return self.__padding


    def getButtonColor(self) -> ButtonColor:
        return self.__btnColor


    def enterEvent(self, event: QEnterEvent):
        super().enterEvent(event)
        self.__isHovered = True

        if self.__btnColor != ButtonColor.PRESSED:
            self.__btnColor = ButtonColor.HOVER
            self.update()



    
    def leaveEvent(self, event: QEvent):
        super().leaveEvent(event)
        self.__isHovered = False

        if self.__btnColor != ButtonColor.PRESSED:
            self.__btnColor = ButtonColor.NORMAL
            self.update()




    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)

        self.__btnColor = ButtonColor.PRESSED
        self.update()




    def mouseReleaseEvent(self, event: QMouseEvent):
        super().mouseReleaseEvent(event)

        if self.__isHovered:
            self.__btnColor = ButtonColor.HOVER
        else:
            self.__btnColor = ButtonColor.NORMAL

        self.update()