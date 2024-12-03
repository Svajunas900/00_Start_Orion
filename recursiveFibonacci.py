from functools import lru_cache
from time import perf_counter


def count_time(func):
    def inner(n):
        start = perf_counter()
        func(n)
        end = perf_counter()
        performance_time = end - start
        return performance_time
    return inner


@count_time
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


@lru_cache
def lru_fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


def cache_fibbonacci(number, cache=None):
    if cache is None:
        cache = {}
    if number in cache:
        return cache[number]
    if number <= 1:
        return number
    result = cache_fibbonacci(number - 2) + cache_fibbonacci(number - 1)
    cache[number] = result
    return result
