from qbclient.Widgets.TitleBar.button import *




class MinimizeButton(TitleBarButton):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)


    def paintEvent(self, _):
        painter = QPainter(self)

        line = QLine(
            0 + self.getPadding(),
            self.height() - self.getPadding(),
            self.width() - self.getPadding(),
            self.height() - self.getPadding()
        )

        pen = QPen(QBrush(self.getButtonColor()), 2)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        painter.setPen(pen)
        painter.drawLine(line)
