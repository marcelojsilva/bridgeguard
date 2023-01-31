from web3 import Web3
import json

class EventListener:
    status = True

    def __init__(self, web3, contract_address, filter, blocknumber = 'latest'):
        print("Listening to filter: ", filter, "status: ", self.status)
        self.w3 = web3
        self.contract_address = contract_address
        self.blocknumber = blocknumber
        self.last_block_processed = web3.eth.blockNumber

        with open("src/listeners/abi.json") as abi_file:
            abi = json.load(abi_file)
            
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)
        self.filter = filter

    async def listen(self):
        for event in self.contract.events[self.filter].createFilter(fromBlock=self.blocknumber).get_new_entries():
            #only process if block is higher than last block processed
            if(self.event_filter(event) and event['blockNumber'] > self.last_block_processed):
                print(self.filter," event received on block ", event['blockNumber'])
                self.on_event(event)
                self.last_block_processed = event['blockNumber']

    def event_filter(self, event):
        return True

    def on_event(self, event):
        pass

    def pretty_print(self, event):
        print(event)

