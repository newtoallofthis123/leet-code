class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for key in nums_dict:
            if nums_dict[key] > 1:
                return True
        return False

solution = Solution().containsDuplicate([1,2,3,1])
print(solution)

# The classic Dictory method
# For some reason, all I am learning by doing this is
# that hashmaps and dictionaries are awesome
# https://leetcode.com/problems/contains-duplicate/submissions/962727209/
