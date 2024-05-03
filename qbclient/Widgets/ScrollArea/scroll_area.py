from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QLayout, QWidget


from qbclient.Widgets.ScrollArea.scroll_bar import ScrollBar



class ScrollArea(QScrollArea):
    def __init__(self, parent: QWidget | None = None, layout: QVBoxLayout | QHBoxLayout = None):
        super().__init__(parent)

        self.__scrollAreaWidgetContents = QWidget(self)
        self.widgets = QFrame(self.__scrollAreaWidgetContents)

        if layout is None:
            layout = QVBoxLayout(self.widgets)
            layout.setSpacing(10)
            layout.setContentsMargins(10, 10, 10, 0)

        self.widgets.setLayout(layout)

        if type(layout) is QVBoxLayout:
            contents_layout = QVBoxLayout(self.__scrollAreaWidgetContents)
        else:
            contents_layout = QHBoxLayout(self.__scrollAreaWidgetContents)

        contents_layout.setSpacing(0)
        contents_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(contents_layout)

        self.setWidget(self.__scrollAreaWidgetContents)
        self.setWidgetResizable(True)

        self.scrollBar = ScrollBar(self, self.__scrollAreaWidgetContents)

        # temp
        self.__scrollAreaWidgetContents.setStyleSheet("background-color: #242831")
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)


    def addWidget(self, widget: QWidget, stretch = 0, aligment_flag: Qt.AlignmentFlag = None):
        widget.setParent(self.widgets)

        if aligment_flag is not None:
            self.widgets.layout().addWidget(widget, stretch, aligment_flag)
        else:
            self.widgets.layout().addWidget(widget, stretch)


    def layout(self) -> QLayout:
        return self.__scrollAreaWidgetContents.layout()

    def setLayout(self, layout: QLayout):
        self.__scrollAreaWidgetContents.setLayout(layout)

        match layout.direction():
            case QVBoxLayout.Direction.TopToBottom:
                af = Qt.AlignmentFlag.AlignTop
            case QVBoxLayout.Direction.BottomToTop:
                af = Qt.AlignmentFlag.AlignBottom
            case QVBoxLayout.Direction.LeftToRight:
                af = Qt.AlignmentFlag.AlignLeft
            case QVBoxLayout.Direction.RightToLeft:
                af = Qt.AlignmentFlag.AlignRight
            case _:
                raise Exception()

        layout.addWidget(self.widgets, 0, af)




    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)

        if self.__scrollAreaWidgetContents.height() - self.height() < 0:
            self.scrollBar.hide()
        else:
            self.scrollBar.show()

        self.scrollBar.updatePosition()


    

