# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n = n // 2
        return True

solution = Solution().isPowerOfTwo(54)
print(solution)

# I had first implemented by calculating divs
# but that was costly
# So, I just used a while loop
# https://leetcode.com/problems/power-of-two/submissions/962761360/
