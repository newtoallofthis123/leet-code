# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        common = []
        for num in nums1:
            if num in nums2:
                common.append(num)
                nums2.remove(num)
        return common
solution = Solution().intersect([1, 2, 2, 1], [2, 2])
print(solution)

# https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/962954350/
# TBH took a little help from AI
# I was not removing the element from nums2, so it was counting the same element again and again