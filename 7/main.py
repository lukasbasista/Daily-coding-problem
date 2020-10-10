""""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """
from typing import List, Optional


class Node:
    __slots__ = ("key", "left", "right")

    def __init__(self) -> None:
        self.key: int = 0
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def foo_help(node):
    if root is None:
        return True, 0

    lb, rb = True, True
    lc, rc = 0, 0

    if node.left is not None:
        lb, lc = foo_help(node.left)

    if node.right is not None:
        rb, rc = foo_help(node.right)

    count = lc + rc

    if lb and rb:
        if node.left is not None and node.key != node.left.key:
            return False, count
        if node.right is not None and node.key != node.right.key:
            return False, count
        return True, count + 1
    return False, count


def foo(root):
    _, count = foo_help(root)
    return count


root = Node()
al = Node()
ar = Node()
bl = Node()
br = Node()
cl = Node()
cr = Node()
root.key = 0
root.left = al
root.right = ar
al.key = 1
ar.key = 0
ar.left = bl
ar.right = br
bl.key = 1
br.key = 0
bl.left = cl
bl.right = cr
cl.key = 1
cr.key = 1

print(foo(root))
