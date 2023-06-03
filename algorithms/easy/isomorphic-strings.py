# https://leetcode.com/problems/isomorphic-strings/
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving 
#the order of characters. No two characters may map to the same character, but a
# character may map to itself.

# Input: s = "egg", t = "add"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i]
            elif s_dict[s[i]] != t[i]:
                return False
            if t[i] not in t_dict:
                t_dict[t[i]] = s[i]
            elif t_dict[t[i]] != s[i]:
                return False
        return True

solution = Solution().isIsomorphic("egg", "add")
print(solution)

# I have to be honest here, I had to look at the solution for this one.
# I was able to come up with a solution that worked for the example, but not for all cases.

# https://leetcode.com/problems/isomorphic-strings/submissions/962746301/
