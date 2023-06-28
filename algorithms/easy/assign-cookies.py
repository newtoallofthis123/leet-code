# https://leetcode.com/problems/assign-cookies/

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        satisfied_children = 0
        for i in range(len(g)):
            for j in range(len(s)):
                if g[i] <= s[j]:
                    satisfied_children += 1
                    s.pop(j)
                    break
        return satisfied_children

solution = Solution().findContentChildren([1,2,3], [1,1])
print(solution)