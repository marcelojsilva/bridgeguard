from .event_listener import EventListener

class BridgeStrangeMintSize(EventListener):
    def __init__(self, web3, contract_address):
        filter = "StandardL2TokenCreated";
        super().__init__(web3, contract_address, filter)

    def on_event(self, event):
        print(f"StandardL2TokenCreated event received: {event}")