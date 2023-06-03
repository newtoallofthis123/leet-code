class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums += [0] * zeros


nums = [0, 0, 1]
Solution().moveZeroes(nums)
print(nums)

# Originally I had uses a while loop because I didn't know about the count function
# in a list
# So, with the help of that, I implemented this.
# https://leetcode.com/problems/move-zeroes/submissions/962944596/
