class Solution:
    def convert(self, num: int) -> str:
        if num < 10:
            return num
        else:
            return chr(ord('a') + num - 10)
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = 2**32 + num
        hexa = ""
        while num > 0:
            hexa = str(self.convert(num % 16)) + hexa
            num //= 16
        return hexa

        
solution = Solution().toHex(26)
print(solution)

# https://leetcode.com/problems/convert-a-number-to-hexadecimal/submissions/962975634/
# The method was quite weird and I didn't know the inbuilt functions
# So, I used help from GitHub Copilot