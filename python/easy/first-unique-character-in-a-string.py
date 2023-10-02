# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in list(s):
            if s.count(i) == 1:
                return s.index(i)
        return -1

solution = Solution().firstUniqChar("aabbb")
print(solution)

# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/962962448/
