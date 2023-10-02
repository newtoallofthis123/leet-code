# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        words = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in words:
                words[sorted_word].append(word)
            else:
                words[sorted_word] = [word]
        for key in words:
            result.append(words[key])
        return result, words


solution = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(solution)

# https://leetcode.com/problems/group-anagrams/submissions/982237516/
# Surprisingly, good and fast solution