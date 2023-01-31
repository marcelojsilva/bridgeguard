from web3 import Web3

class connectionProvider:
    ERROR_CANT_CONNECT = "Could not connect to WS RPC server"

    def __init__(self, name, url):
        self.ws_name = name
        self.url = url

    def connect(self, is_http=False):
        web3 = is_http ? Web3(Web3.HTTPProvider(self.url)) : Web3(Web3.WebsocketProvider(self.url))
        if not web3.isConnected():
            self.onError(self.ERROR_CANT_CONNECT)
            return
        print("Connected to WS RPC server:", self.name)
        return web3

    def onError(self, error):
        print("Error connecting to WS RPC server: ", self.name, "Error: ", error)
