# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 4 != 0:
                return False
            n = n // 4
        return True

solution = Solution().isPowerOfFour(12)
print(solution)

# https://leetcode.com/problems/power-of-four/submissions/962921415/