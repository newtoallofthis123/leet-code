class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ideal = len(nums)/2
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for num in num_dict:
            if num_dict[num] > ideal:
                return num

solution = Solution().majorityElement([3, 2, 3])
print(solution)

# https://leetcode.com/problems/majority-element/submissions/981118747/