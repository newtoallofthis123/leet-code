class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 2 == 0:
            n = n / 2

        while n % 3 == 0:
            n = n / 3

        while n % 5 == 0:
            n = n / 5

        return n == 1

solution = Solution().isUgly(24)
print(solution)

# First I was finding the factors of the number
# But that was costly
# So, CoPilot suggested to use a while loop
# https://leetcode.com/problems/ugly-number/submissions/962778229/
# however, I found a better solution
# class Solution:
#     def isUgly(self, n: int) -> bool:
#         if(n == 0): return False
#         for x in [2, 3, 5]:
#             while(n%x == 0):
#                 n = n//x
#         return n==1