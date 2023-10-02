class Solution(object):
    def isIncreaingMonotonic(self, nums):
        i = 0
        # increasing part
        while i < len(nums)-1:
            if nums[i] <= nums[i+1]:
                i = i+1
            else:
                return False
        return True 
    
    def isDecreasingMonotonic(self, nums):
        i = 0
        # decreasing part
        while i < len(nums)-1:
            if nums[i] >= nums[i+1]:
                i = i+1
            else:
                return False
        return True

    def isMonotonic(self, nums):
        if len(nums) == 1:
            return True
        
        i = 0
        if nums[i] < nums[i+1]:
            return self.isIncreaingMonotonic(nums)
        elif nums[i] > nums[i+1]:
            return self.isDecreasingMonotonic(nums)
        elif nums[i] == nums[i+1]:
            if not self.isIncreaingMonotonic(nums[1:]):
                return self.isDecreasingMonotonic(nums[1:])
            else:
                return self.isIncreaingMonotonic(nums[1:])
        

# Test
solution = Solution()
print(solution.isMonotonic([3]))


"""
[1, 1, 0]
"""