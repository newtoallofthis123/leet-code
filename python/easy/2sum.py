# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            for j in range(i+1,len(nums)):
                if num + nums[j] == target:
                    return [i,j]
                
solution = Solution().twoSum([2,7,11,15],9)
print(solution)

# A simple implementation using two for loops
# https://leetcode.com/problems/two-sum/submissions/962955007/