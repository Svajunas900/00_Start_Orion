from recursiveFibonacci import fibonacci


class Fibo:
    def fibonacci(self, number_1):
        if number_1 <= 1:
            return number_1
        else:
            return self.fibonacci(number_1-2) + self.fibonacci(number_1-1)

fibo = Fibo()

print(fibo.fibonacci(5))