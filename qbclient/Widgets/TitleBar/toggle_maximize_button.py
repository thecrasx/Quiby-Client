from qbclient.Widgets.TitleBar.button import *




class ToggleMaximizeButton(TitleBarButton):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.__isMaximized = False
        self.setPadding(15)


    def setMaximize(self, maximize: bool):
        if maximize and not self.__isMaximized:
            self.setPadding(self.getPadding() * 1.5)
            self.__isMaximized = True
        
        elif not maximize and self.__isMaximized:
            self.setPadding(self.getPadding() / 1.5)
            self.__isMaximized = False


    def toggleMaximize(self):
        self.setMaximize(not self.__isMaximized)



    def paintEvent(self, _):
        painter = QPainter(self)

        # Center
        cx = round(self.width() / 2)
        cy = round(self.height() / 2)

        spacer =  self.width() * 0.1

        xpad = self.getPadding() * (self.width() / 100 * 1.3) 
        ypad = self.getPadding() * (self.height() / 100 * 1.3) 

        top = 0 + ypad
        left = 0 + xpad
        right = self.width() - xpad
        bottom = self.height() - ypad

        # TOP LEFT CORNER - Horizontal
        line_1 = QLine(left, top, cx - spacer, top)

        # TOP LEFT CORNER - Vertical
        line_2 = QLine(left, top, top, cy - spacer)

        # TOP RIGHT CORNER - Horizontal
        line_3 = QLine(cx + spacer, top, right, top)

        # TOP RIGHT CORNER - Vertical
        line_4 = QLine(right, top, right, cy - spacer)

        # BOTTOM RIGHT CORNER - Horizontal
        line_6 = QLine(right, bottom, cx + spacer, bottom)

        # BOTTOM RIGHT CORNER - Vertical
        line_5 = QLine(right, cy + spacer,right, bottom)

        # BOTTOM LEFT CORNER - Horizontal
        line_7 = QLine(cx - spacer, bottom, top, bottom)

        # BOTTOM LEFT CORNER - Vertical
        line_8 = QLine(top, cy + spacer, top, bottom)

        pen = QPen(QBrush(self.getButtonColor()), 2)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        painter.setPen(pen)
        painter.drawLines([
            line_1, line_2, line_3, line_4,
            line_5, line_6, line_7, line_8
        ])
