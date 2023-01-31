from .event_listener import EventListener
from web3 import Web3
import src.log as log

mylogger = log.get_logger(__name__)

class BridgeUnsualValue(EventListener):
    def __init__(self, web3, contract_address):
        self.counter = 0
        filter_event = "DepositFinalized"
        super().__init__(web3, contract_address, filter_event, 'latest')

    def event_filter(self, event):
        amount = Web3.fromWei(event.args._amount, 'ether')
        if(amount >= 100):
            return True

    def on_event(self, event):
        self.status = False
        mylogger.info("Listening to filter: DepositFinalized status:", self.status)

