# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        s = list(s)
        for i in t:
            if i not in s:
                return i
            else:
                s.remove(i)

solution = Solution().findTheDifference("a", "aa")
print(solution)

# https://leetcode.com/problems/find-the-difference/submissions/962968284/
