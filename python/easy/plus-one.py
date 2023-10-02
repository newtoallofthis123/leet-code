# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join([str(i) for i in digits])) + 1
        return [int(i) for i in str(num)]

solution = Solution().plusOne([1, 2, 3])        

# https://leetcode.com/problems/plus-one/submissions/962422896/