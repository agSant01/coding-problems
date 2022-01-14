en
class Node(object):
    def __init__(self, heap, current=0) -> None:
        right = 2 * current + 2
        self.right = Node(heap, right) if right < len(
            heap) and heap[right] is not None else None

        left = 2 * current + 1
        self.left = Node(heap, left) if left < len(
            heap) and heap[left] is not None else None

        self.value = heap[current]


def find_ancestor(tree, ancestor_list=None):
    if tree is None:
        return

    if ancestor_list is None:
        ancestor_list = []
    else:
        ancestor_list.append(tree.value)

    find_ancestor(tree.left, ancestor_list)
    find_ancestor(tree.right, ancestor_list)

    return ancestor_list


def find_ancestor_iterative(tree: Node):
    stack = []
    ancestor_list = []

    stack.append(tree.right)
    stack.append(tree.left)

    while len(stack) != 0:
        unvisited_ancestor = stack.pop()

        if unvisited_ancestor is None:
            continue

        ancestor_list.append(unvisited_ancestor.value)

        stack.append(unvisited_ancestor.right)
        stack.append(unvisited_ancestor.left)

    return ancestor_list


tree1 = Node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
res = find_ancestor(tree1)
print(res)

tree2 = Node([1, 2, 3, 4, 5])
res = find_ancestor(tree2)
print(res)


tree3 = Node([1])
res = find_ancestor(tree3)
print(res)

print('Iterative: ')
res = find_ancestor_iterative(tree1)
print(res)
res = find_ancestor_iterative(tree2)
print(res)
res = find_ancestor_iterative(tree3)
print(res)
