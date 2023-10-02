# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = ""
        if '-' in str(x):
            rev += '-'
        x = str(x).strip('-')
        for i in range(len(x)):
            rev += x[len(x) - i-1]

        num = int(rev)
        if num > -1*pow(2, 31) and num < pow(2, 31) -1:
            return num        
        return 0

solution = Solution()
print(solution.reverse(-123))

# That was easy
# Thanks to python

# Solution
# https://leetcode.com/problems/reverse-integer/submissions/960937314/