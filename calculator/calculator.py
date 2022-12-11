import math


class Calculator:

    def __init__(self, statement):
        self.statement = statement

    def calculate(self):
        result = eval(self.statement)
        return result
