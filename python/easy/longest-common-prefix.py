#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = max(strs, key=len)
        for i, char in enumerate(longest):
            for j in strs:
                if j[i] != char:
                    return longest[:i]
        return longest

solution = Solution().longestCommonPrefix(["flower","flow","flight"])
print(solution)

# !TODO