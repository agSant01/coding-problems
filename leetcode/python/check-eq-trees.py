class Node(object):
    def __init__(self, heap, current=0) -> None:
        right = 2 * current + 2
        self.right = Node(heap, right) if right < len(
            heap) and heap[right] is not None else None

        left = 2 * current + 1
        self.left = Node(heap, left) if left < len(
            heap) and heap[left] is not None else None

        self.value = heap[current]


def are_equal(tree1: Node, tree2: Node):
    if tree1 is None and tree2 is None:
        return True

    if tree1 is None or tree2 is None:
        return False

    if tree1.value != tree2.value:
        return False

    return are_equal(tree1=tree1.left, tree2=tree2.left) and \
        are_equal(tree1=tree1.right, tree2=tree2.right)


tree1 = Node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tree2 = Node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
res = are_equal(tree1, tree2)
print(res)

tree1 = Node([1, 2, 3, 4])
tree2 = Node([1, 2, 3, ])
res = are_equal(tree1, tree2)
print(res)

tree1 = Node([1, 2, 3, 4])
tree2 = Node([1, 2, 3, 5])
res = are_equal(tree1, tree2)
print(res)

tree1 = Node([1, 2, 3, 4])
tree2 = Node([1, -1, 3, 5])
res = are_equal(tree1, tree2)
print(res)

tree1 = Node([1, 2, 3, 4, None, None, 7, 8, 9, 10])
tree2 = Node([1, 2, 3, 4, None, None, 7, 8, 9, 10])
res = are_equal(tree1, tree2)
print(res)
