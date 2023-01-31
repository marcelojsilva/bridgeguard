from .event_listener import EventListener

class BridgeStrangeMintSize(EventListener):
    def __init__(self, web3, contract_address):
        filter = "StandardL2TokenCreated"
        super().__init__(web3, contract_address, filter, 'latest')

    def on_event(self, event):
        self.status = False
        print("Listening to filter: StandardL2TokenCreated status:", self.status)
