from recursiveFibonacci import fibonacci


class Fibo:

    def __init__(self, number: int):
        self.number = number

    def fibonacci(self, number: int) -> int:
        if number <= 1:
            return number
        else:
            return self.fibonacci(number - 2) + self.fibonacci(number - 1)

    def get_fibonnaci_number(self):
        return self.fibonacci(self.number)


fibo = Fibo(6)

print(fibo.get_fibonnaci_number())
