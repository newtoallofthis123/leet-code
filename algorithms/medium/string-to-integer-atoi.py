# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0
        num = ""
        if s[0] == "-":
            num += "-"
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            else:
                break
        if len(num) == 0 or num == "-":
            return 0
        if int(num) > 2**31 - 1:
            return 2**31 - 1
        elif int(num) < -2**31:
            return -2**31

        return int(num)

solution = Solution()
print(solution.myAtoi("words and 89"))

# Uses a lot of memory, but it works
# https://leetcode.com/problems/string-to-integer-atoi/submissions/941091948/