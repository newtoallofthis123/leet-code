import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = math.sqrt(num)
        if root.is_integer():
            return True
        else:
            return False
    
solution = Solution().isPerfectSquare(14)
print(solution)

# https://leetcode.com/problems/valid-perfect-square/submissions/962956899/
# Without using inbuilt functions
# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         if num == 1:
#             return True
#         for i in range(2, num):
#             if i * i == num:
#                 return True
#             elif i * i > num:
#                 return False
#         return False