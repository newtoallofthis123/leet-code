# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        return None

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0

obj = MyQueue()
obj.push(2)
obj.push(3)
obj.push(5)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2, param_3, param_4)

# Runtime is quite high, but it works.
# https://leetcode.com/problems/implement-queue-using-stacks/submissions/962766533/
