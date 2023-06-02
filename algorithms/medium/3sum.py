class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        total = 0
        result = []
        nums.sort()

        for i, current in enumerate(nums):
            if i > 0 and current == nums[i - 1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                total = current + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    result.append([current, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result
            
solution = Solution().threeSum([-1,0,1,2,-1,-4])
print(solution)

# TBH I used AI to solve this problem. I was stuck on this problem for a long time. I was trying to use two pointers to solve this problem.
# I had intially used a brute force approach to solve this problem.
# I just used combinations and it exceeded the memory limit. 
# Hence, today I learnt about back tracking
# Using Permuation and Combinations is a good way to solve back tracking problems.
"""
permuts = list(combinations(nums, 3))
results =  [list(i) for i in permuts if sum(i) == 0]
results = list(set([tuple(result) for result in results]))
return [list(result) for result in results]
This is how I solved it using combinations.
"""
# https://youtu.be/jzZsG8n2R9A

# Solved it finally after watching this video. I was trying to use two pointers to solve this problem.
# https://leetcode.com/problems/3sum/submissions/962531557/
