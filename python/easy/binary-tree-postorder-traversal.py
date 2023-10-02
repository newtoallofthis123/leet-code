# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: list[TreeNode]) -> list[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.val, node.right, node.left])
            elif isinstance(node, int):
                result.append(node)
        
        return result

solution = Solution()
print(solution.postorderTraversal([1,None,2,3])) # [3,2,1]

# https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/977855406/
