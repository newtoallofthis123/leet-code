# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from itertools import product
        phone = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        choosen = [phone[digit] for digit in digits]
        combinations = []
        for combination in product(*choosen):
            combinations.append(''.join(combination))
        if combinations == [""]:
            return []
        return combinations

solution = Solution().letterCombinations("235")
print(solution)

# Can be better implemented with DFS and BFS using stacks

# Solution
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/960999524/