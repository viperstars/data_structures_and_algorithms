class QueueOverflow(ValueError):
    pass


class SQueue(object):
    def __init__(self, length=8):
        self.length = length
        self.elements = [0] * self.length
        self.head = 0
        self.num = 0

    def is_empty(self):
        return self.num == 0

    def peek(self):
        if self.is_empty():
            raise QueueOverflow
        return self.head

    def dequeue(self):
        if self.is_empty():
            raise QueueOverflow
        p = self.elements[self.head]
        self.head = (self.head + 1) % self.length
        self.num -= 1
        return p

    def enqueue(self, p):
        if self.num == self.length:
            self.extend()
        self.elements[(self.head + self.num) % self.length] = p
        self.num += 1

    def extend(self):
        old_len = self.length
        self.length *= 2
        new_elements = [0] * self.length
        for i in range(old_len):
            new_elements[i] = self.elements[(self.head + i) % old_len]
        self.elements, self.head = new_elements, 0


class PriorityQueue(object):
    def __init__(self, lst=[]):
        self.elements = list(lst)
        if lst:
            self.heap()

    def is_empty(self):
        return not self.elements

    def peek(self):
        if self.is_empty():
            raise QueueOverflow("in peek")
        return self.elements[0]

    def enqueue(self, e):
        self.elements.append(None)
        self.shiftup(e, len(self.elements) - 1)

    def shiftup(self, e, last):
        elems, i, j = self.elements, last, (last - 1) / 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 2) / 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise
        elems = self.elements
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.shiftup(e, 0, len(elems))
        return e0

    def shiftdown(self, e, begin, end):
        elems, i, j = self.elements, begin, begin * 2
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    def heap(self):
        end = len(self.elements)
        for i in range(end // 2, -1, -1):
            self.shiftdown(self.elements[i], i, end)
