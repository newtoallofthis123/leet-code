# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [i for i in arr if i < pivot]
            mid = [i for i in arr if i == pivot]
            right = [i for i in arr if i > pivot]
            return quick_sort(left) + mid + quick_sort(right)
        nums.append(target)
        nums = quick_sort(nums)
        return nums.index(target)

solution = Solution().searchInsert([1,3,5,6], 2)
print(solution)

# https://leetcode.com/problems/search-insert-position/submissions/962939004/
# I mean wow. I am shocked at how people think of implementations
# Mine was rather lousy
# But I like quick sort so