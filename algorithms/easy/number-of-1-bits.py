# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        one_count = 0
        while n:
            one_count += n & 1
            n >>= 1

solution = Solution().hammingWeight(00000000000000000000000000001011)
print(solution)

# https://leetcode.com/problems/number-of-1-bits/submissions/981851339/
