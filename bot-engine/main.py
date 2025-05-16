
from memory import Memory
from onchain_storage import store_message, get_messages
import asyncio

memory = Memory()

async def main():
    print("Chavrick Bot AI Engine Starting...")
    while True:
        message = input("User: ")
        memory.add_message(message)
        await store_message(message)
        print("Bot:", memory.get_messages())

if __name__ == "__main__":
    asyncio.run(main())
