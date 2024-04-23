from qbclient.Widgets.TitleBar.button import *




class ExitButton(TitleBarButton):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)


    def paintEvent(self, _):
        painter = QPainter(self)

        line_1 = QLine(
            0 + self.getPadding(),
            0 + self.getPadding(),
            self.width() - self.getPadding(),
            self.height() - self.getPadding()
        )

        line_2 = QLine(
            self.width() - self.getPadding(),
            0 + self.getPadding(),
            0 + self.getPadding(),
            self.height() - self.getPadding(),
        )

        pen = QPen(QBrush(self.getButtonColor()), 2)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        painter.setPen(pen)
        painter.drawLine(line_1)
        painter.drawLine(line_2)
