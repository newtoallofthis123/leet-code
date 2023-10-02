# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Whenever you need to find sum, use hoare's partitioning algorithm
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l+1, r+1]

solution = Solution().twoSum([0, 0, 3, 4], 0)
print(solution)

# I used help for this one, but I understand it now.
# From Now on, whenever I need to find sum, I will use hoare's partitioning algorithm
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/962757517/
