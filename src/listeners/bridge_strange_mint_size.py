from .event_listener import EventListener
import src.log as log

mylogger = log.get_logger(__name__)

class BridgeStrangeMintSize(EventListener):
    def __init__(self, web3, contract_address):
        filter_event = "StandardL2TokenCreated"
        super().__init__(web3, contract_address, filter_event, 'latest')

    def on_event(self, event):
        self.status = False
        mylogger.info("Listening to filter: StandardL2TokenCreated status:", self.status)
