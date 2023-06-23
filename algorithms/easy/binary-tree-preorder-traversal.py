# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: list[TreeNode]) -> list[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.right, node.left, node.val])
            elif isinstance(node, int):
                result.append(node)
        return result

solution = Solution()
print(solution.preorderTraversal([1,None,2,3])) # [1,2,3]