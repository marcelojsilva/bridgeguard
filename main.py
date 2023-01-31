# import the following dependencies
import asyncio
import src.settings as settings

#load all listeners
from src.providers.connection_provider import connectionProvider
from src.listeners.bridge_strange_mint_size import BridgeStrangeMintSize
from src.listeners.bridge_messenger_owner_changed import BridgeMessengerOwnerChanged
from src.listeners.bridge_unsual_value import BridgeUnsualValue
from src.listeners.bridge_proxy_owner_changed import BridgeProxyOwnerChanged
from src.mempool.bridge_pending_transactions_count import PendingTransactionsCounter
#create a hello world python
async def main():
    # Connect to websocket
    web3L1 = connectionProvider(settings.NETWORK_NAME, settings.NETWORK, False).connect()

    # Start listener
    #bridgeStrangeMintSizeListener = BridgeStrangeMintSize(web3L1, settings.CONTRACT_ADDRESS)
    #bridgeMessengerOwnerChangedListener = BridgeMessengerOwnerChanged(web3L1, settings.CONTRACT_ADDRESS)
    bridgePendingTransactionsCountListener = PendingTransactionsCounter(web3L1, settings.CONTRACT_ADDRESS)
    
    #bridgeUnsualValue = BridgeUnsualValue(web3L1, settings.CONTRACT_ADDRESS)
    #bridgeProxyOwnerChanged = BridgeProxyOwnerChanged(web3L1, settings.CONTRACT_ADDRESS)
    
    while True:
        #await asyncio.create_task(bridgeStrangeMintSizeListener.listen())
        #await asyncio.create_task(bridgeMessengerOwnerChangedListener.listen())
        await asyncio.create_task(bridgePendingTransactionsCountListener.validate())
        print("sleep")
        await asyncio.sleep(10)
        #await asyncio.create_task(bridgeUnsualValue.listen())
        #await asyncio.create_task(bridgeProxyOwnerChanged.listen())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")


