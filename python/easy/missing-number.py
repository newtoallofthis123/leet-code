# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        all_nums = list(range(0, len(nums)+1))
        for num in all_nums:
            if num not in nums:
                return num
        return None

solution = Solution().missingNumber([3, 0, 1])
print(solution)

# https://leetcode.com/problems/missing-number/submissions/962931925/
