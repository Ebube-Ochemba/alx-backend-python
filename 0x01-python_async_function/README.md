# Python - Async

> This project was an introduction to async programming in Python.

## Summary

I learnt about `async` and `await` syntax, how to execute an async program with asyncio, how to run concurrent coroutines, how to create asyncio tasks, and how to use the random module.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-basic_async_syntax.py](https://github.com/Ebube-Ochemba/alx-backend-python/blob/main/0x01-python_async_function/0-basic_async_syntax.py): An asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.
    - Use the `random` module.
- [x] [1-concurrent_coroutines.py](https://github.com/Ebube-Ochemba/alx-backend-python/blob/main/0x01-python_async_function/1-concurrent_coroutines.py): An async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`.
- [x] [2-measure_runtime.py](https://github.com/Ebube-Ochemba/alx-backend-python/blob/main/0x01-python_async_function/2-measure_runtime.py): A `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a float.
    - Use the `time` module to measure an approximate elapsed time.
- [x] [3-tasks.py](https://github.com/Ebube-Ochemba/alx-backend-python/blob/main/0x01-python_async_function/3-tasks.py): A function `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`. (do not create an async function, use the regular function syntax to do this)
- [x] [4-tasks.py](https://github.com/Ebube-Ochemba/alx-backend-python/blob/main/0x01-python_async_function/4-tasks.py): Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

> [test_files](./test_files): A folder of test files. Provided by Alx.
