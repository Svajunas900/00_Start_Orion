def uppercase(func):
    def inner(a_string):
        return a_string.upper()
    return inner


@uppercase
def helloworld(b_string):
    return b_string


print(helloworld("Hello world"))
