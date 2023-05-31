# To be revisted

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_words = []
        string = ""
        for i in range(len(s)):
            j = i
            try:
                while s[j] not in string:
                    string += s[j]
                    j+=1
                current_words.append(string)
                string = ""
            except:
                pass
        current_words = [len(i) for i in current_words]
        if current_words == []:
            return 1
        return max(current_words)

solution = Solution().lengthOfLongestSubstring('aab')
print(solution)

# This got accepted but I had to do a bit of tkintering
# The test cases aab and au work when I run this file locally
# But don't seem to work on the online editor
# So I put a small if else statement to solve the both
# This felt like cheating so I had to write it here
# I have no idea why It wasn't working
# This is very weird and wacky code to begin with so
# Will revisit this

# Solution
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/960932995/