# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        to_reach = n
        choices = [choice for choice in range(1, n)]
        # TODO: Implement a recursive function that returns the number of ways to reach the top

print(Solution().climbStairs(3))