import socket

from qbclient.Connection.response import *

class ServerConfig:
    IP: str = socket.gethostname()
    PORT = 54345

    def getAddress() -> tuple[str, int]:
        return (ServerConfig.IP, ServerConfig.PORT)







class Connection:
    def __init__(self, IP: str = ServerConfig.IP, PORT: int = ServerConfig.PORT):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((IP, PORT))

        self.responseSignals = ResponseSignals(self)

        self.__running: bool = False


    def __routeResponse(self, response):
        match response['action']:
            case 'login':
                self.responseSignals.login.emit(response)
            case 'register':
                self.responseSignals.register.emit(response)
            case 'message':
                self.responseSignals.message.emit(response)
            case _:
                print("No valid route")
                print(response)



    def stop(self):
        if self.__running: self.__running = False




    def listen(self):
        self.__running = True
        while self.__running:
            try:
                msg = self.server.recv(1024).decode()
                print(msg)
                self.__routeResponse(msg)


            except Exception as e:
                print(e)
                self.stop()


    def send(self, data):
        pass












