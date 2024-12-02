from functools import lru_cache


def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number-2) + fibonacci(number-1)


@lru_cache
def lru_fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number-2) + fibonacci(number-1)


print(fibonacci(5))
print(lru_fibonacci(5))