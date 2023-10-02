# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            nums.sort()
            return nums[-3]                

solution = Solution().thirdMax([1, 2])
print(solution)

# https://leetcode.com/problems/third-maximum-number/submissions/962980708/
