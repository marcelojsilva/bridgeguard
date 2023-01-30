
# import the following dependencies
import json
import asyncio
import os
from dotenv import load_dotenv
from src.providers.wsProvider import wsProvider


#PYTHONPATH="/Users/alexandremelo/projects/0pwatcher:$PYTHONPATH"
#export PYTHONPATH

load_dotenv("src/.env")

#create a hello world python
def main():
    # Connect to websocket
    wsRpcL1EndPoint = os.getenv("WS_RPC_L1")
    wsRpcL1Name = os.getenv("WS_RPC_L1_NAME")
    web3L1 = wsProvider(wsRpcL1Name, wsRpcL1EndPoint).connect()

if __name__ == "__main__":
    main()


