from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


from qbclient.Connection.response import ResponseType

class AuthWidget(QWidget):
    def __init__(self, parent: QWidget | None, conn):
        super().__init__(parent)
        self.show()


    def __checkInputData(self, register: bool = False) -> bool:
        # Email / Username input
        # Password input
        # Confirm Password input
        # Date check
        pass



    def login(self):
        pass


    def register(self):
        pass


    def __onServerResponse(self, response):
        if response.type == ResponseType.LOGIN:
            pass

        elif response.type == ResponseType.REGISTER:
            pass








if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv[0])
    widget = AuthWidget(None, '')
    sys.exit(app.exec())