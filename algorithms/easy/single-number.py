# https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for num in num_dict:
            if num_dict[num] < 2:
                return num

solution = Solution().singleNumber([2, 2, 1])
print(solution)