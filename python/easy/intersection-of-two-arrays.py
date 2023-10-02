# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums = set(nums1).intersection(set(nums2))
        return list(nums)

solution = Solution().intersection([1,2,2,1], [2,2])
print(solution)

# https://leetcode.com/problems/intersection-of-two-arrays/submissions/962946941/