# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: list[TreeNode]) -> bool:
        def compare(p, q):
            if p and q:
                return p.val == q.val and compare(p.left, q.right) and compare(p.right, q.left)
            return p == q
        return compare(root, root)

solution = Solution()
print(solution.isSymmetric([1,2,2,3,4,4,3])) # True