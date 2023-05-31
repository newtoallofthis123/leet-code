# Gokaraju Zindabad

# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        is_valid = True
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for item in s:
            if item in pairs.keys():
                stack.append(item)
            elif item in pairs.values():
                if len(stack) == 0 or pairs[stack.pop()] != item:
                    is_valid = False
                    break
        
        if len(stack) > 0:
            is_valid = False
        
        return is_valid

solution = Solution().isValid('[')
print(solution)

# Uses a simple hashmap. Have to admit, used AI a bit

# Solution
# https://leetcode.com/problems/valid-parentheses/submissions/961018019/