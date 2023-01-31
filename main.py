import asyncio
import src.settings as settings
from src.providers.connection_provider import connection_provider
from src.listeners.bridge_strange_mint_size import BridgeStrangeMintSize
from src.listeners.bridge_messenger_owner_changed import BridgeMessengerOwnerChanged
from src.listeners.bridge_unsual_value import bridge_unsual_value
from src.listeners.bridge_proxy_owner_changed import bridge_proxy_owner_changed
import src.log as log

mylogger = log.get_logger(__name__)

async def main():
    # Connect to websocket
    web3_l1 = connection_provider(settings.HTTP_RPC_HH, settings.WS_RPC_L1_NAME, True).connect()

    # Start listener
    bridge_strange_mint_size_listener = BridgeStrangeMintSize(web3_l1, settings.CONTRACT_ADDRESS)
    bridge_messenger_owner_changed_listener = BridgeMessengerOwnerChanged(web3_l1, settings.CONTRACT_ADDRESS)
    bridge_unsual_value = bridge_unsual_value(web3_l1, settings.CONTRACT_ADDRESS)
    bridge_proxy_owner_changed = bridge_proxy_owner_changed(web3_l1, settings.CONTRACT_ADDRESS)
    
    while True:
        await asyncio.create_task(bridge_strange_mint_size_listener.listen())
        await asyncio.create_task(bridge_messenger_owner_changed_listener.listen())
        await asyncio.create_task(bridge_unsual_value.listen())
        await asyncio.create_task(bridge_proxy_owner_changed.listen())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        mylogger.info("Exit")



