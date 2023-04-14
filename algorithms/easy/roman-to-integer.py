# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = s
        convert = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1 
        }
        total = 0
        to_add = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and convert[s[i]] < convert[s[i+1]]:
                to_add = convert[s[i+1]] - convert[s[i]]
                i += 2
            else:
                to_add = convert[s[i]]
                i += 1
            total += to_add
        return total
    
# https://leetcode.com/problems/roman-to-integer/submissions/933527551/
# Stupid Error!