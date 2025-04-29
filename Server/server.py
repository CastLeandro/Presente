from fastapi import FastAPI

class Server:
    def __init__(self) -> None:
        self.versao = '0.1'
        self.app = FastAPI(version=self.versao, title= 'Presente-api')


server = Server()
