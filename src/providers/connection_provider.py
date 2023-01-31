from web3 import Web3

class connectionProvider:
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
            self.onError(self.ERROR_CANT_CONNECT)
            return
        print("Connected to WS RPC server:", self.name)
        return web3

    def onError(self, error):
        print("Error connecting to WS RPC server: ", self.name, "Error: ", error)
