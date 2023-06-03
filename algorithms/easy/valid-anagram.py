# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
        for key in s_dict:
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False
        return True

solution = Solution().isAnagram(s="anagram", t="nagaram")
print(solution)

# A simple implementations using dictionaries.
# First gets the count of each character and systamatically compares them.
# https://leetcode.com/problems/valid-anagram/submissions/962917532/
