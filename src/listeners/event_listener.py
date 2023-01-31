from web3 import Web3
import json

class EventListener:
    def __init__(self, web3, contract_address, filter):
        self.w3 = web3
        self.contract_address = contract_address
        
        with open("src/listeners/abi.json") as abi_file:
            abi = json.load(abi_file)
            
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)
        self.filter = filter

    async def listen(self):
        for event in self.contract.events[self.filter].createFilter(fromBlock='latest').get_new_entries():
            self.on_event(event)

    def on_event(self, event):
        pass
