import pytest
from recursiveFibonacci import fibonacci, lru_fibonacci
from FiboClass import Fibo
from decorator import helloworld

def test_fibonnaci():
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(-1) == -1
    assert fibonacci(10) == 55

def test_lru_fibonnaci():
    assert lru_fibonacci(5) == 5
    assert lru_fibonacci(6) == 8
    assert lru_fibonacci(-1) == -1
    assert lru_fibonacci(10) == 55

def test_Fibo():
    fibo = Fibo(5)
    assert fibo.fibonacci(5) == 5
    assert fibo.fibonacci(6) == 8
    assert fibo.fibonacci(-1) == -1
    assert fibo.fibonacci(10) == 55

def test_helloWorld():
    assert helloworld("hello world") == "HELLO WORLD"
    