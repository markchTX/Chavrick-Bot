
from memory import Memory
from onchain_storage import store_message, get_messages

memory = Memory()

async def main():
    while True:
        message = input("User: ")
        memory.add_message(message)
        await store_message(message)
        print("Bot:", memory.get_messages())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
