"""
2^-4 = 1/2 * 1/2 * 1/2 * 1/2

2^4 = 16
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or n==1:
            return 1.0
        elif n<0:
            return 1/self.myPow(x, -n)
        else:
            return x * self.myPow(x, n-1)
    
solution = Solution()
print(solution.myPow(2.0, -3))

# https://leetcode.com/problems/powx-n/submissions/1094396756
# Not satisfied, try again after learning bit manipulation
