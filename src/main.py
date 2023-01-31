# import the following dependencies
import json
import asyncio
import os
from dotenv import load_dotenv

#load all listeners
from src.providers.connection_provider import connectionProvider
from src.listeners.bridge_strange_mint_size import BridgeStrangeMintSize
from src.listeners.bridge_messenger_owner_changed import BridgeMessengerOwnerChanged
from src.listeners.bridge_unsual_value import BridgeUnsualValue
from src.listeners.bridge_proxy_owner_changed import BridgeProxyOwnerChanged

load_dotenv("src/.env")

#create a hello world python
async def main():
    # Connect to websocket
    wsRpcL1EndPoint = os.getenv("HTTP_RPC_HH")
    wsRpcL1Name = os.getenv("WS_RPC_L1_NAME")
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    web3L1 = connectionProvider(wsRpcL1Name, wsRpcL1EndPoint, True).connect()

    # Start listener
    bridgeStrangeMintSizeListener = BridgeStrangeMintSize(web3L1, contractAddress)
    bridgeMessengerOwnerChangedListener = BridgeMessengerOwnerChanged(web3L1, contractAddress)
    bridgeUnsualValue = BridgeUnsualValue(web3L1, contractAddress)
    bridgeProxyOwnerChanged = BridgeProxyOwnerChanged(web3L1, contractAddress)
    
    while True:
        await asyncio.create_task(bridgeStrangeMintSizeListener.listen())
        await asyncio.create_task(bridgeMessengerOwnerChangedListener.listen())
        await asyncio.create_task(bridgeUnsualValue.listen())
        await asyncio.create_task(bridgeProxyOwnerChanged.listen())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")


