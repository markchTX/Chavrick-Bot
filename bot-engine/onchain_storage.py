
import os
from solana.rpc.async_api import AsyncClient
from dotenv import load_dotenv

load_dotenv()

WSS_ENDPOINT = os.getenv("WSS_ENDPOINT")
RPC_ENDPOINT = os.getenv("RPC_ENDPOINT")

client = AsyncClient(RPC_ENDPOINT)

async def store_message(message):
    print(f"Storing message on-chain: {message}")
    # TODO: Implement PDA-based storage logic

async def get_messages():
    print("Fetching messages from on-chain...")
    # TODO: Implement PDA-based fetch logic
