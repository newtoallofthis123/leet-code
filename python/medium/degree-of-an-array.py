class Solution(object):
    def findShortestSubArray(self, nums):
        map = {}

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        max_degree = max(map.values())
        min_length = float("inf")

        for key, value in map.items():
            if value == max_degree:
                first = nums.index(key)
                last = len(nums) - nums[::-1].index(key) - 1
                min_length = min(min_length, last - first + 1)

        return min_length


solution = Solution()
print(solution.findShortestSubArray([1, 2, 2, 3, 1]))
