# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: list[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    
# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/977867134/
