# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ""
        for i in s:
            if i.isalnum():
                string += i
        string = string.upper()
        if(''.join(reversed(list(string))) == string):
            return True
        else:
            return False

solution = Solution().isPalindrome("0p")
print(solution)