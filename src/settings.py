import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

HTTP_RPC_HH = os.getenv("HTTP_RPC_HH")
WS_RPC_L1_NAME = os.getenv("WS_RPC_L1_NAME")
