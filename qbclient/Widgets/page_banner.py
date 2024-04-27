from PySide6.QtGui import QFont, QColor, QPen, QBrush, QPainter, QPolygonF, QResizeEvent
from PySide6.QtCore import Qt, QPointF, QRectF
from PySide6.QtWidgets import QWidget



class PageBanner(QWidget):
    def __init__(self, text, parent: QWidget | None = None):
        super().__init__(parent)

        self.__text = text
        self.__pointList = [
            (QPointF(0, 0)),
            (QPointF(0, self.height() / 2)),
            (QPointF(self.width() / 2, self.height())),
            (QPointF(self.width(), self.height() / 2)),
            (QPointF(self.width(), 0))
        ]

        self.__font = QFont()
        self.__font.setPointSize(12)

        self.show()




    def setText(self, text: str):
        self.__text = text
        self.update()


    def setFont(self, font: QFont):
        self.__font = font
        self.update()



    
    def paintEvent(self, _):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # Polygon
        brush = QBrush(QColor("#1E1F22"))
        painter.setBrush(brush)

        painter.drawPolygon(QPolygonF(self.__pointList))

        # Text
        pen = QPen(QColor("#989BA5"))
        painter.setPen(pen)

        painter.setFont(self.__font)
        painter.drawText(
            QRectF(0, 0, self.width(), self.height() * 0.85),
            self.__text,
            Qt.AlignmentFlag.AlignCenter
        )

    


    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self.__pointList[1].setY(self.height() / 2)

        self.__pointList[2].setX(self.width() / 2)
        self.__pointList[2].setY(self.height())

        self.__pointList[3].setX(self.width())
        self.__pointList[3].setY(self.height() / 2)

        self.__pointList[4].setX(self.width())


