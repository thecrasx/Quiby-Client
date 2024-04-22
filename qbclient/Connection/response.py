from PySide6.QtCore import QObject, Signal




class ResponseSignals(QObject):
    login = Signal(str)
    register = Signal(str)
    message = Signal(str)


