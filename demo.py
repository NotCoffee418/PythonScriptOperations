import asyncio
import operation_manager


def add():
    return 5 + 7


def subtract():
    return 12 - 4


async def multiply_async():
    await asyncio.sleep(1)  # Simulate some async processing
    return 6 * 3


def divide():
    print(f"{36 / 6} (without a returned value)")


# Register the operations
operation_manager.register_operation(add, "Addition: 5 + 7")
operation_manager.register_operation(subtract, "Subtraction: 12 - 4")
operation_manager.register_operation(
    multiply_async, "Multiplication (async): 6 * 3")
operation_manager.register_operation(divide, "Division: 36 / 6")

if __name__ == "__main__":
    print("Welcome to the math demo of our operation manager!")
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(operation_manager.start_listening_async())
        # operation_manager.start_listening() # Without async
    finally:
        loop.close()
