# Exercise_01
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()

    def is_full(self):
        return len(self.stack) == self.capacity

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None


def devide(a, b):
    return a/b


def abc():
    return 1
