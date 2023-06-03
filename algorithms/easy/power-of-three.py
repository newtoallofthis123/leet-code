# https: // leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 3 != 0:
                return False
            n = n // 3
        return True

solution = Solution().isPowerOfThree(22)
print(solution)

# https://leetcode.com/problems/power-of-three/submissions/962920137/
