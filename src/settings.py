import os
from dotenv import load_dotenv

load_dotenv(".env")

NETWORK = os.getenv("WS_RPC_L1")
NETWORK_NAME = os.getenv("WS_RPC_L1_NAME")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")