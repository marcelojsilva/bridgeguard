import src.log as log

class PendingTransactionsCounter():
    def __init__(self, web3, contract_address, threshold=10):
        self.threshold = threshold
        self.web3 = web3
        self.contract_address = contract_address
        self.pending_tx_count = 0
        self.status = True
        self.logger = log.get_logger(__name__)
        self.logger.info("PendingTransactionsCounter started");

    async def validate(self):
        async with self.web3 as ws:
            subscription = await ws.eth_subscribe("newPendingTransactions")
            while True:
                tx = await subscription.get_next_entries()
                print(tx)
                if tx['to'] == self.contract_address:
                    self.pending_tx_count += 1

    # def check_threshold(self):
    #     if self.pending_tx_count >= self.threshold:
    #         self.status = False
    #         self.logger.info("Listening to counter: PendingTransactionsCounter status: %s", self.status)
