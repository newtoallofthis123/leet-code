class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        if x <= pow(2, 31) - 1:
            # Use higher precision to avoid rounding errors
            return int(round(math.sqrt(x), 10))

# https://leetcode.com/problems/sqrtx/submissions/933710822/
# Very messy implementation but it works
# Time complexity: O(log(n))
# Space complexity: O(1)