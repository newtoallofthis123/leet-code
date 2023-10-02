# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
            if i == len(s):
                return True
        return False

solution = Solution().isSubsequence("abc", "ahbgdc")
print(solution)

# https://leetcode.com/problems/is-subsequence/submissions/962978994/
