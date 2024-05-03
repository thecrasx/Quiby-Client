from PySide6.QtGui import QPainter, QColor, QIcon, QPixmap
from os.path import exists as path_exists

from qbclient.Widgets.Icon.color import IconColor
from qbclient.Widgets.Icon.state import State, StateIcon




class Icon:
    def __init__(self, path: str = "", icon_color: IconColor = IconColor()):
        self.__path: str = path
        self.__pixmap = QPixmap()

        self.__iconColor = icon_color
        self.__stateIcon = StateIcon()

        self.load(path)
        self.__iconColor.iconColorChanged.connect(self.__onIconColorChanged)




    def filePath(self) -> str:
        return self.__path


    def iconColor(self) -> IconColor:
        return self.__iconColor


    def setIconColor(self, icon_color: IconColor):
        self.__iconColor = icon_color
        self.__makeIcons()




    def load(self, path: str = "", icon_color: IconColor = None):
        if path != "":
            if not path_exists(path):
                raise FileNotFoundError(path)
            
            else:
                self.__pixmap = QPixmap(path)

                if icon_color is not None:
                    self.setIconColor(icon_color)
                else:
                    self.__makeIcons()




    def get(self, state: State = None) -> QIcon:
        match state:
            case State.PRESS:
                return self.__stateIcon.press
            case State.HOVER:
                return self.__stateIcon.hover
            case State.SELECT:
                return self.__stateIcon.select
            case State.NORMAL | _:
                return self.__stateIcon.normal




    def __onIconColorChanged(self, state: State):
        match state:
            case State.NORMAL:
                self.__stateIcon.normal = self.__makeIcon(state)
            case State.PRESS:
                self.__stateIcon.press = self.__makeIcon(state)
            case State.HOVER:
                self.__stateIcon.hover = self.__makeIcon(state)
            case State.SELECT:
                self.__stateIcon.select = self.__makeIcon(state)



    
    def __makeIcon(self, state: State) -> QIcon:
        pixmap = self.__pixmap.copy()
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), self.__getIconColor(state))
        painter.end()
        return QIcon(pixmap)



    
    def __makeIcons(self):
        self.__stateIcon.normal = self.__makeIcon(State.NORMAL)
        self.__stateIcon.press = self.__makeIcon(State.PRESS)
        self.__stateIcon.hover = self.__makeIcon(State.HOVER)
        self.__stateIcon.select = self.__makeIcon(State.SELECT)




    def __getIconColor(self, state: State) -> QColor:
        match state:
            case State.NORMAL:
                return self.__iconColor.normal
            case State.PRESS:
                return self.__iconColor.press
            case State.HOVER:
                return self.__iconColor.hover
            case State.SELECT:
                return self.__iconColor.select
            case _:
                return IconColor.DEFAULT










    









        