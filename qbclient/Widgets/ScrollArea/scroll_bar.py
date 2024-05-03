from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *



class ScrollBar(QFrame):
    def __init__(self, parent: QScrollArea, scroll_area_widget_contents: QWidget):
        super().__init__(parent)

        self.setStyleSheet("background-color: #6821bf;")
        self.setFixedSize(10, 30)
        self.move(self.x(), 5)

        self.scrollAreaWidgetContents = scroll_area_widget_contents
        self.__padding: tuple[int, int] = (5, 5)
        self.__pressed = False
        self.__increment = 10

        vs: QScrollBar = self.parent().verticalScrollBar()
        vs.valueChanged.connect(self.__onScrollBarValueChange)
        # vs.rangeChanged.connect(self.__onScrollbarRangeChange)




    def __onScrollBarValueChange(self, val: int):
        if not self.__pressed:
            height = self.parent().height() - self.height() - (self.__padding[1] * 2)

            v = self.calculateValue(
                    y1 = 0,
                    y2 = val,
                    y3 = self.parent().verticalScrollBar().maximum()
                )

            self.move(
                self.x(),
                (height * v) + self.__padding[1]
            )

    def __onScrollbarRangeChange(self):
        p = self.parent().height() - ((self.scrollAreaWidgetContents.height() - self.parent().height()) * 2)
        if p > 0:
            self.setHeight(p)
            self.setIncrement(p)



    def setPadding(self, lr: int, tb: int):
        self.__padding(lr, tb)

    def setIncrement(self, size):
        self.__increment = round(size / self.height())

    def setHeight(self, h: int):
        if h >= 30:
            self.setFixedHeight((h * 0.8) - self.__padding[1])



    
    def calculateScrollValue(self) -> float:
        y1 = self.__padding[1] # start
        y2 = self.parent().height() - self.height() - self.__padding[1] # end
        assert(y2 > y1)
        return (self.y() - y1) / (y2 - y1)




    def calculateValue(self, y1, y2, y3) -> float:
        assert(y3 >= y2 and y2 >= y1)
        return (y2 - y1) / (y3 - y1)


    
    def updatePosition(self):
        self.move(self.parent().width() - self.width() - self.__padding[0], self.y())




    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self.updatePosition()




    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)
        self.dragPos = event.globalPosition().toPoint()
        self.__pressed = True




    def mouseReleaseEvent(self, event: QMouseEvent):
        super().mouseReleaseEvent(event)
        self.__pressed = False




    def mouseMoveEvent(self, event: QMouseEvent):
        super().mouseMoveEvent(event)

        if event.buttons() == Qt.LeftButton:
            y = (self.pos() + event.globalPosition().toPoint() - self.dragPos).y()
            max_y = self.parent().height() - self.height() - self.__padding[1]

            if y >= self.__padding[1] and y <= max_y:
                p = self.scrollAreaWidgetContents.height() - self.parent().height()
                if p > 0:
                    self.move(self.x(), y)

                    vs: QScrollBar = self.parent().verticalScrollBar()
                    vs.setValue(vs.maximum() * self.calculateScrollValue())


                    self.dragPos = event.globalPosition().toPoint()

            event.accept()

    