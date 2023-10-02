# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution(object):
    def sortEvenOdd(self, nums):
        i = 0
        odds = []
        evens = []
        while i<len(nums):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
            i+= 1

        odds = list(sorted(odds)[::-1])
        evens = list(sorted(evens))

        result = []
        i = 0
        while i<max(len(evens), len(odds)):
            if i < len(evens):
                result.append(evens[i])
            if i< len(odds):
                result.append(odds[i])
            i+=1

        return result

solution = Solution()
print(solution.sortEvenOdd([2, 1]))

"""
[2, 4]
[3, 1]
"""