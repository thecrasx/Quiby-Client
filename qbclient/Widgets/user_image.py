from PySide6.QtWidgets import QWidget, QFrame, QSizePolicy
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainterPath, QPaintEvent, QPainter, QPen, QBrush, QImage, QResizeEvent

from PIL import Image




class UserImage(QFrame):
    def __init__(self, parent: QWidget | None = None, path: str = ""):
        super().__init__(parent)
        self.show()

        self.__imgWidth = 0
        self.__image = None
        self.__path = path
        if path != "":
            self.setImage(path)

        sp = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sp.setHeightForWidth(True)
        self.setSizePolicy(sp)



    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)

        self.cropImageFromCenter(self.height() * 0.5)


    def setImage(self, path: str):
        if self.__image is None:
            self.__image = QImage(path)
        else:
            self.__image.load(path)


        self.__imgWidth = self.__image.width()
        self.setFixedSize(self.__imgWidth, self.__imgWidth)


    def resizeImage(self, wh: int):
        img = Image.open(self.__path)
        self.__image = img.resize((wh, wh)).toqimage()
        self.__imgWidth = self.__image.width()
        self.setFixedSize(self.__imgWidth, self.__imgWidth)


    def cropImageFromCenter(self, wh: int):
        img = Image.open(self.__path)

        box = (
            img.size[0] / 2 - wh, img.size[1] / 2 - wh,
            img.size[0] / 2 + wh, img.size[1] / 2 + wh
        )

        self.__image = img.crop(box).toqimage()

        self.__imgWidth = self.__image.width()
        self.setFixedSize(self.__imgWidth, self.__imgWidth)




    def paintEvent(self, event: QPaintEvent):
        super().paintEvent(event)
        if self.__image is None:
            return
        painter = QPainter(self)
        painter.setBackgroundMode(Qt.BGMode.TransparentMode)
        painter.setRenderHint(QPainter.Antialiasing, True)
        
        radius = round(self.__imgWidth / 2)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.__imgWidth, self.__imgWidth, radius, radius)

        xy = self.__imgWidth * 0.6
        wh = self.__imgWidth * 0.3
        path.addRoundedRect(xy, xy, wh, wh, wh / 2, wh / 2)

        painter.setClipPath(path)
        painter.drawImage(0, 0, self.__image)

        brush = QBrush(Qt.GlobalColor.green)
        pen = QPen(brush, 0)
        painter.setPen(pen)
        painter.setClipping(False)
        painter.setBrush(brush)

        xy = self.__imgWidth * 0.75
        rxy = self.__imgWidth * 0.1
        painter.drawEllipse(QPoint(xy, xy), rxy, rxy)

        
