from .event_listener import EventListener

class BridgeStrangeMintSize(EventListener):
    def __init__(self, web3, contract_address):
        filter = "StandardL2TokenCreated"
        #get current block
        self.last_block_processed = web3.eth.blockNumber
        print(f"last_block_processed: {self.last_block_processed}")
        super().__init__(web3, contract_address, filter, 'latest')

    def on_event(self, event):
        block_number = event['blockNumber']
        if block_number > self.last_block_processed:
            print(f"StandardL2TokenCreated event received: {event}")
            self.last_block_processed = block_number
