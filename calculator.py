from operations.addition import add
from operations.subtraction import subtract
from operations.multiplication import multiply
from operations.division import divide
from operations.exponentiation import exponentiate
from operations.modulus import modulus

class Calculator:
    def add(self, a, b):
        return add(a, b)

    def subtract(self, a, b):
        return subtract(a, b)

    def multiply(self, a, b):
        return multiply(a, b)

    def divide(self, a, b):
        return divide(a, b)

    def exponentiate(self, a, b):
        return exponentiate(a, b)

    def modulus(self, a, b):
        return modulus(a, b)
