"""
Asyncio Example - Demonstrating basic async/await functionality in Python

This example shows how to use asyncio to run multiple coroutines concurrently.
The example uses a simple dialogue between two characters to illustrate the concept.
"""
import asyncio


async def q():
    """First coroutine that prints a message and waits for 3 seconds."""
    print("시트웰: 답이 하나도 안 맞잖아?")
    await asyncio.sleep(3)  # Simulating an I/O operation that takes 3 seconds


async def a():
    """Second coroutine that prints a message immediately."""
    print("로저스: 하지만 빨랐죠.")


async def main():
    """Main coroutine that gathers and runs both coroutines concurrently."""
    await asyncio.gather(q(), a())


if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine until it completes
