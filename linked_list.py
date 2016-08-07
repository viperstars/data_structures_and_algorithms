class LinkedListOverflow(ValueError):
    pass


class LinkedListNode(object):
    def __init__(self, element, next_node=None):
        self.element = element
        self.next = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, element):
        self.head = LinkedListNode(element, next_node=self.head)

    def pop_first(self):
        if self.is_empty():
            raise LinkedListOverflow("in pop_first")
        element = self.head.element
        self.head = self.head.next_node
        return element

    def append(self, element):
        if self.is_empty():
            self.head = LinkedListNode(element)
            return
        p = self.head
        while p is not None:
            p = p.next_node
        p.next_node = LinkedListNode(element)

    def pop_last(self):
        if self.is_empty():
            raise LinkedListOverflow("in pop_last")
        p = self.head
        if p.next_node is None:
            q = self.head.element
            self.head = None
            return q
        while p.next_node.next_node is None:
            p = p.next_node
        q = p.next_node.element
        p.next_node = None
        return q
