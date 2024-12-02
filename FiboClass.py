from recursiveFibonacci import fibonacci


class Fibo:

    def __init__(self, number):
        self.number = number

    def fibonacci(self):
        if self.number <= 1:
            return self.number
        else:
            return Fibo(self.number-2).fibonacci() + Fibo(self.number-1).fibonacci()


fibo = Fibo(6)

print(fibo.fibonacci())