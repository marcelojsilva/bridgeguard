from web3 import Web3

class wsProvider:
    ERROR_CANT_CONNECT = "Could not connect to WS RPC server"

    def __init__(self, ws_name, ws_url):
        self.ws_name = ws_name
        self.ws_url = ws_url

    def connect(self):
        web3 = Web3(Web3.WebsocketProvider(self.ws_url))
        if not web3.isConnected():
            self.onError(self.ERROR_CANT_CONNECT)
            return
        print("Connected to WS RPC server:", self.ws_name)
        return web3

    def onError(self, error):
        print("Error connecting to WS RPC server: ", self.ws_name, "Error: ", error)
