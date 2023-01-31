from web3 import Web3
import src.log as log

mylogger = log.get_logger(__name__)

class connection_provider:
    ERROR_CANT_CONNECT = "Could not connect to WS RPC server"

    def __init__(self, name, url, is_http=False):
        self.name = name
        self.url = url
        self.is_http = is_http

    def connect(self):
        if self.is_http:
            web3 = Web3(Web3.HTTPProvider(self.url))
        else:
            web3 = Web3(Web3.WebsocketProvider(self.url))

        if not web3.isConnected():
            self.on_error(self.ERROR_CANT_CONNECT)
            return
        mylogger.info("Connected to WS RPC server:", self.name)
        return web3

    def on_error(self, error):
        mylogger.error("Error connecting to WS RPC server: ", self.name, "Error: ", error)
