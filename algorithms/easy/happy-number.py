# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not .

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_sum(num:int):
            total = sum([int(i)**2 for i in str(num)])
            return total
        
        tries = 0
        is_happy = False
        while tries < 1000:
            n = get_sum(n)
            if n == 1:
                is_happy = True
                break
            tries += 1
        
        return is_happy
    
solution = Solution().isHappy(19)
print(solution)

# I am not happy with this solution. It is almost 50ms.
# That is way too close to the time limit
# And it is kinda a basic solution
# https://leetcode.com/problems/happy-number/submissions/962719711/
