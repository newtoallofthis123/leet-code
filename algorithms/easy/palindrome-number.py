# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not x >= pow(-2, 31) or not x <= pow(2, 31):
            return False

        string = str(x)
        if string == string[::-1]:
            return True
        else:
            return False

# Submitted
# Not very good run time, but hey
# https://leetcode.com/problems/palindrome-number/submissions/933486027/