import json
import logging
from web3 import Web3

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class EventListener:
    status = True

    def __init__(self, web3, contract_address, filter, blocknumber='latest'):
        self.status = True
        self.w3 = web3
        self.contract_address = contract_address
        self.blocknumber = blocknumber
        self.last_block_processed = web3.eth.blockNumber

        with open("src/listeners/abi.json") as abi_file:
            abi = json.load(abi_file)
            
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)
        self.filter = filter
        logger.info("%s event listener started", self.filter)

    async def listen(self):
        for event in self.contract.events[self.filter].createFilter(fromBlock=self.blocknumber).get_new_entries():
            if (self.event_filter(event) and event['blockNumber'] > self.last_block_processed):
                logger.info("%s event received:", self.filter)
                logger.info(" - block: %d", event['blockNumber'])
                logger.info(" - tx: %s", event['transactionHash'].hex())
                logger.info(" - contract: %s", self.contract_address)

                self.on_event(event)
                self.last_block_processed = event['blockNumber']

    def event_filter(self, event):
        return True

    def on_event(self, event):
        pass
