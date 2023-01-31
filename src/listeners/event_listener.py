import json
from web3 import Web3
import src.log as log

mylogger = log.get_logger(__name__)

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
        mylogger.info("%s event listener started", self.filter)

    async def listen(self):
        for event in self.contract.events[self.filter].createFilter(fromBlock=self.blocknumber).get_new_entries():
            if (self.event_filter(event) and event['blockNumber'] > self.last_block_processed):
                mylogger.info("%s event received:", self.filter)
                mylogger.info(" - block: %d", event['blockNumber'])
                mylogger.info(" - tx: %s", event['transactionHash'].hex())
                mylogger.info(" - contract: %s", self.contract_address)

                self.on_event(event)
                self.last_block_processed = event['blockNumber']

    def event_filter(self, event):
        return True

    def on_event(self, event):
        pass
