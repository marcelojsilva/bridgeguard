from .event_listener import EventListener
from web3 import Web3

class BridgeUnsualValue(EventListener):
    def __init__(self, web3, contract_address):
        self.counter = 0
        filter = "DepositFinalized"
        super().__init__(web3, contract_address, filter, 'latest')

    def event_filter(self, event):
        amount = Web3.fromWei(event.args._amount, 'ether')
        if(amount >= 100):
            return True

    def on_event(self, event):
        self.status = False
        print("Listening to filter: DepositFinalized status:", self.status)

