def uppercase(func):
    def inner(a_string):
        return a_string.upper()
    return inner


@uppercase
def helloworld(b_string):
    return b_string


def odd_number(func):
    def inner(n):
        result = func(n)
        if result % 2 == 1:
            return result
        return "Fibo result is not an odd value"
    return inner
