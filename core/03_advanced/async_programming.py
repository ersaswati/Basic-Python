"""
File: async_programming.py
Description:
    Demonstrates asynchronous programming used in API-based AI systems.
Author: Saswati Barik
Level: Advanced
"""

import asyncio

# 🔹 Example: Async function

async def fetch_data(a, b):
    print("Fetching data...")
    await asyncio.sleep(1)  # simulate async operation
    result = a + b
    print(f"Data fetched, result: {result}")
    return result


# asyncio.run(fetch_data())
# Expected Output:
# Fetching data...
# Data fetched
