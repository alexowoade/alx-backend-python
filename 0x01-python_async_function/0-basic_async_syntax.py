#!/usr/bin/env python3

"""
This module demonstrates the basics of asynchronous programming in Python.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that generates a random delay and waits for that amount of time before returning.

    Args:
        max_delay (int, optional): The maximum amount of time to wait before returning, in seconds.
            Defaults to 10.

    Returns:
        float: The amount of time waited, in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

