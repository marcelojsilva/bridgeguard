from .event_listener import EventListener

class BridgeStrangeMintSize(EventListener):
    def __init__(self, web3, contract_address):
        filter = "StandardL2TokenCreated"
        self.last_block_processed = 0
        super().__init__(web3, contract_address, filter, 'latest')

    def on_event(self, event):
        block_number = event['blockNumber']
        if block_number > self.last_block_processed:
            print(f"StandardL2TokenCreated event received: {event}")
            self.last_block_processed = block_number
