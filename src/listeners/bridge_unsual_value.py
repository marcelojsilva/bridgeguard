from listerner import EventListener

class BridgeStrangeSize(EventListener):
    def __init__(self, web3, contract_address):
        filter = self.contract.events.StandardL2TokenCreated.createFilter(fromBlock='latest')
        super().__init__(web3, contract_address, filter)


    def event_filter(self, event):
        #validate if event emitDepositFinalized amount is bigger then 100
        if(event.amount > 100):
            return True

    def on_event(self, event):
        print(f"StandardL2TokenCreated event received: {event}")