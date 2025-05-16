
import os
from solana.rpc.async_api import AsyncClient
from dotenv import load_dotenv

load_dotenv()

RPC_ENDPOINT = os.getenv("RPC_ENDPOINT")
PROGRAM_ID = os.getenv("PROGRAM_ID")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

client = AsyncClient(RPC_ENDPOINT)

async def store_message(message):
    print(f"Storing message on-chain: {message}")
    # TODO: Implement PDA-based storage logic

async def get_messages():
    print("Fetching messages from on-chain...")
    # TODO: Implement PDA-based fetch logic
