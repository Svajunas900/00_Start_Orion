import pytest
from recursiveFibonacci import fibonacci, lru_fibonacci
from FiboClass import Fibo
from decorator import helloworld


def test_fibonnaci():
    assert fibonacci(5) == 5, "Provided number isn't == 5"
    assert fibonacci(6) == 8, "Provided number isn't == 8"
    assert fibonacci(-1) == -1, "Provided number isn't == -1"
    assert fibonacci(10) == 55, "Provided number isn't == 55"


def test_lru_fibonnaci():
    assert lru_fibonacci(5) == 5, "Provided number isn't == 5"
    assert lru_fibonacci(6) == 8, "Provided number isn't == 8"
    assert lru_fibonacci(-1) == -1, "Provided number isn't == -1"
    assert lru_fibonacci(10) == 55, "Provided number isn't == 55"


def test_Fibo():
    fibo = Fibo(6)
    assert fibo.get_fibonnaci_number() == 5, "Provided number isn't == 5"
    assert fibo.get_fibonnaci_number() == 8, "Provided number isn't == 8"
    assert fibo.get_fibonnaci_number() == -1, "Provided number isn't == -1"
    assert fibo.get_fibonnaci_number() == 55, "Provided number isn't == 55"


def test_helloWorld():
    assert helloworld("hello world") == "HELLO WORLD"
