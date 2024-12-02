from recursiveFibonacci import fibonacci


class Fibo:
    def __init__(self, number):
        self.number = number

    def fibonacci(self, number_1):
        if number_1 <= 1:
            return number_1
        else:
            return self.fibonacci(number_1-2) + self.fibonacci(number_1-1)

fibo = Fibo(5)

print(fibo.fibonacci(5))