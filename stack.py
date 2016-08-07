class StackOverflow(ValueError):
    pass


class SStack(object):
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def top(self):
        if self.is_empty():
            raise StackOverflow("in top")
        return self.elements[-1]

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            raise StackOverflow("in pop")
        return self.elements.pop()
