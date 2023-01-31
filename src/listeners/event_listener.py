from web3 import Web3
import json

class EventListener:
    status = True

    def __init__(self, web3, contract_address, filter, blocknumber):
        print("Listening to filter: ", filter, "status: ", self.status)
        self.w3 = web3
        self.contract_address = contract_address
        self.blocknumber = blocknumber
        
        with open("src/listeners/abi.json") as abi_file:
            abi = json.load(abi_file)
            
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)
        self.filter = filter

    async def listen(self):
        for event in self.contract.events[self.filter].createFilter(fromBlock=self.blocknumber).get_new_entries():
            if(self.event_filter(event)):
                self.on_event(event)
                #self.pretty_print(event)

    def event_filter(self, event):
        return True

    def on_event(self, event):
        pass

    def pretty_print(self, event):
        print(event)

