# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                magazine.remove(i)
        return True

solution = Solution().canConstruct("aa","ab")
print(solution)

# https://leetcode.com/problems/ransom-note/submissions/962959291/