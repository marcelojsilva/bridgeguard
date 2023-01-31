from .event_listener import EventListener
import src.log as log

mylogger = log.get_logger(__name__)

class BridgeMessengerOwnerChanged(EventListener):
    def __init__(self, web3, contract_address):
        filter_event = "OwnershipTransferred"
        super().__init__(web3, contract_address, filter_event, 'latest')

    def event_filter(self, event):
        return True

    def on_event(self, event):
        self.status = False
        mylogger.info("Listening to filter: OwnershipTransferred status:", self.status)
