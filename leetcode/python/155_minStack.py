class MinStackNode:
    class Node:
        def __init__(self, val, min_, next_):
            self.val = val
            self.min_ = min_
            self.next_ = next_

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head:
            nn = MinStackNode.Node(val, min(val, self.head.min_), self.head)
            self.head = nn
        else:
            self.head = MinStackNode.Node(val, val, None)

    def pop(self) -> None:
        self.head = self.head.next_

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_


class MinStackList:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
