from functools import lru_cache
from time import perf_counter
from decorator import odd_number


def count_time(func):
    def inner(n):
        start = perf_counter()
        func(n)
        end = perf_counter()
        performance_time = end - start
        return performance_time
    return inner


def fibonacci(number: int) -> int:
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


@odd_number
def get_fibo(number: int) -> int:
    return fibonacci(number)


@lru_cache
def lru_fibonacci(number: int) -> int:
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


def cache_fibbonacci(number: int, cache=None) -> int:
    if cache is None:
        cache = {}
    if number in cache:
        return cache[number]
    if number <= 1:
        return number
    result = cache_fibbonacci(number - 2) + cache_fibbonacci(number - 1)
    cache[number] = result
    return result

