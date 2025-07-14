import math
import json


class Calculator:
    def _init__(self):
        self.result = 0.0
        self.undo_stack = []
        self.redo_stack = []
        self.variables = {}

    def _push_undo(self):
        self.undo_stack.append(self.result)
        self.redo_stack.clear()        # reset redo when new action happens.

    def create_variable(self, name):
        self.variables[name] = self.result

    def get_variable(self, name):
        return self.variables.get(name, self.result)

    def set_variable(self, name):
        if name in self.variables:
            self.variables[name] = self.result

    def add(self, value):
        self._push_undo()
        self.result += value

    def subtract(self, value):
        self._push_undo()
        self.result -= value

    def multiply(self, value):
        self._push_undo()
        self.result *= value

    def divide(self, value):
        if value == 0:
            raise ValueError("Cannot divide by zero.")
        self._push_undo()
        self.result /= value

    def mod(self, value):
        self._push_undo()
        self.result %= value

    def square(self):
        self._push_undo()
        self.result **= 2

    def square_root(self):
        if self.result < 0:
            raise ValueError("Cannot take square root of a negative number.")
        self._push_undo()
        self.result = math.sqrt(self.result)

    def exponent(self, value):
        self._push_undo()
        self.result = math.pow(self.result, value)

    def factorial(self):
        if self.result < 0 or not float(self.result).is_integer():
            raise ValueError(
                "Factorial is only defined "
                "for non-negative integers.")
        self._push_undo()
        self.result = math.factorial(int(self.result))

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.result)
            self.result = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.result)
            self.result = self.redo_stack.pop()

    def clear(self):
        self.result = 0.0
        self.undo_stack.clear()
        self.redo_stack.clear()
        self.variables.clear()
