class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def cal_depth(self, root):
        if root is None:
            return 0

        left_depth = self.cal_depth(root.left)
        right_depth = self.cal_depth(root.right)

        if left_depth == -1 or right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1

    def isBalanced(self, root):
        return self.cal_depth(root) != -1

solution = Solution()
print(
    solution.isBalanced(
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    )
)
