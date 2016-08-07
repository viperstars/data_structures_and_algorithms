from stack import SStack
from queue import SQueue, PriorityQueue


class BinaryTreeByList(object):
    def __init__(self, root=None, left=None, right=None):
        self.tree = [root, left, right]

    def is_node(self):
        return self.tree[0] is not None and self.tree[1] is None and self.tree[2] is None

    def root(self):
        return self.tree[0]

    def left(self):
        return self.tree[1]

    def right(self):
        return self.tree[2]

    def set_root(self, root):
        self.tree[0] = root

    def set_left(self, left):
        self.tree[1] = left

    def set_right(self, right):
        self.tree[2] = right


class BinaryTreeNode(object):
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def is_node(self):
        return self.left is None and self.right is None


def count(tree):
    if not tree:
        return 0
    if tree.is_node():
        return 1
    else:
        return 1 + count(tree.left) + count(tree.right)


a = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4)), BinaryTreeNode(3))


def sums(tree):
    if not tree:
        return 0
    else:
        return tree.root + sums(tree.left) + sums(tree.right)


def pre_order(tree, func):
    if not tree:
        return
    else:
        func(tree.root)
    if tree.left is not None:
        pre_order(tree.left, func)
    if tree.right is not None:
        pre_order(tree.right, func)


def pre_order_nr(tree, func):
    s = SStack()
    while tree or not s.is_empty():
        while tree:
            func(tree.root)
            s.push(tree.right)
            tree = tree.left
        tree = s.pop()


def level_order(tree, func):
    q = SQueue()
    q.enqueue(tree)
    while not q.is_empty():
        tree = q.dequeue()
        if tree is None:
            continue
        q.enqueue(tree.left)
        q.enqueue(tree.right)
        func(tree.root)


class HuffmanTreeNode(BinaryTreeNode):
    def __lt__(self, htn):
        return self.root < htn.root


class HuffmanPriorityQueue(PriorityQueue):
    def number(self):
        return len(self.elements)


def build_huffman_tree(weights):
    trees = HuffmanPriorityQueue()
    for w in weights:
        trees.enqueue(HuffmanTreeNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.root + t2.root
        trees.enqueue(HuffmanTreeNode(x, t1, t2))
    return trees.dequeue()
