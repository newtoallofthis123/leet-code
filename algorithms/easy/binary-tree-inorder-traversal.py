# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: list[TreeNode]) -> list[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.right, node.val, node.left])
            elif isinstance(node, int):
                result.append(node)

solution = Solution()
print(solution.inorderTraversal([1,None,2,3])) # [1,3,2]

# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/977853440/
