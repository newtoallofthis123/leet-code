# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """    
        # return haystack.find(needle) # This would do the trick. But I guess it's not the point of the exercise.
        first = haystack
        second = needle
        for i in range(len(first)):
            if first[i:i+len(second)] == second:
                return i
        return -1
    
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/962407676/
