# https://leetcode.com/problems/implement-stack-using-queues/
from collections import deque

class MyStack(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0

obj = MyStack()
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2, param_3, param_4)

# I implemented the normal one using arrays before
# But it's space complexity is too high
# So I tried to use deque
# Now it's run time is much faster
# https://leetcode.com/problems/implement-stack-using-queues/submissions/962725426/
