#!/usr/bin/env python3
"""Altered wait_n using task_wait_random"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    Returns the list of all the delays (float values) in ascending order
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
