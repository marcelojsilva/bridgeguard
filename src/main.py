# import the following dependencies
import json
import asyncio
import os
from dotenv import load_dotenv
from src.providers.connection_provider import connectionProvider
from src.listeners.bridge_strange_mint_size import BridgeStrangeMintSize

load_dotenv("src/.env")

#create a hello world python
async def main():
    # Connect to websocket
    wsRpcL1EndPoint = os.getenv("HTTP_RPC_HH")
    wsRpcL1Name = os.getenv("WS_RPC_L1_NAME")
    contractAddress = os.getenv("CONTRACT_ADDRESS")

    web3L1 = connectionProvider(wsRpcL1Name, wsRpcL1EndPoint, True).connect()

    # Start listener
    listener = BridgeStrangeMintSize(web3L1, contractAddress)
    
    while True:
        await asyncio.create_task(listener.listen())

if __name__ == "__main__":
    asyncio.run(main())
