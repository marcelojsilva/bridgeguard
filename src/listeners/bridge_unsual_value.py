from .event_listener import EventListener

class BridgeUnsualValue(EventListener):
    def __init__(self, web3, contract_address):
        filter = "DepositFinalized"
        super().__init__(web3, contract_address, filter, 'latest')

    def event_filter(self, event):
        if(event.amount >= 50e18):
            return True

    def on_event(self, event):
        self.status = False