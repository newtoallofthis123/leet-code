# https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums:list[int], k:int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        duplicates = {}
        for i in range(len(nums)):
            if nums[i] in duplicates and i - duplicates[nums[i]] <= k:
                return True
            duplicates[nums[i]] = i
        return False
    
solution = Solution().containsNearbyDuplicate([1,2,3,4], 3)
print(solution)

# I use a simple hash map to store the index of the last occurrence of each element.
# Then I check if the element has been seen before and if the last occurrence is within the given distance k.
# If both conditions are true, then we found a duplicate within the given distance.

# https://leetcode.com/problems/contains-duplicate-ii/submissions/962733304/
