# https://leetcode.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
    
# https://leetcode.com/problems/add-binary/submissions/933706862/
# Quite Easy