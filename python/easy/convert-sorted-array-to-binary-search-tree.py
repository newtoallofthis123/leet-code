# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> list[TreeNode]:
        pivot = len(nums) // 2
        root = TreeNode(nums[pivot])
        if pivot > 0:
            root.left = self.sortedArrayToBST(nums[:pivot])
        if pivot < len(nums) - 1:
            root.right = self.sortedArrayToBST(nums[pivot + 1:])
        return root
    
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/977864765/

# Didn't know how to do this one, so I looked at the solution. I was on the right track, but I didn't know how to
# implement it.