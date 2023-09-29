# https://leetcode.com/problems/sort-array-by-parity/

class Solution(object):
    def sortArrayByParity(self, nums):
        evens = []
        odds = []
        for num in nums:
            if num %2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        for odd in odds:
            evens.append(odd)

        return evens

solution = Solution()
print(solution.sortArrayByParity([3,1,2,4]))