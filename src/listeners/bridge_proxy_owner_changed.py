from .event_listener import EventListener

class BridgeProxyOwnerChanged(EventListener):
    def __init__(self, web3, contract_address):
        filter = "AddressSet"
        super().__init__(web3, contract_address, filter, 'latest')

    def event_filter(self, event):
        return True

    def on_event(self, event):
        self.status = False
        print("Listening to filter: AddressSet status:", self.status)
