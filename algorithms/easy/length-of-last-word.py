# https://leetcode.com/problems/length-of-last-word/

"""
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        raw = s.split(" ")
        for i in range(len(raw)):
            if raw[len(raw)-i-1] != '':
                return len(raw[len(raw)-i-1])


solution = Solution()
solution.lengthOfLastWord("   fly me   to   the moon  ")

# Solved
# https://leetcode.com/problems/length-of-last-word/submissions/937527007/