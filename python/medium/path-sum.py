class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )


solution = Solution()
print(
    solution.hasPathSum(
        TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
            TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
        ),
        22,
    )
)
print(solution.hasPathSum(TreeNode(), 22))
