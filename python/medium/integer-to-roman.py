# https://leetcode.com/problems/integer-to-roman

class Solution(object):
    def intToRoman(self, num:int)->str:
        """
        :type num: int
        :rtype: str
        """
        symbols = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100:'C',
            500:'D',
            1000:'M'
        }
        temp = num
        roman = ''
        digits = []
        while temp > 0:
            digits.append(temp % 10)
            temp = temp // 10
        digits = [digit * (10 ** i) for i, digit in enumerate(digits)]
        digits.reverse()
        for digit in digits:
            if digit in symbols:
                roman += symbols[digit]
            else:
                # I just handle all the cases
                # I know it's not the best way
                # but it's the fastest way to solve this problem
                if digit < 5:
                    if digit == 4:
                        roman += symbols[1] + symbols[5]
                    else:
                        roman += symbols[1] * digit
                elif digit < 10:
                    if digit == 9:
                        roman += symbols[1] + symbols[10]
                    else:
                        roman += symbols[5] + symbols[1] * (digit - 5)
                elif digit < 50:
                    if digit == 40:
                        roman += symbols[10] + symbols[50]
                    else:
                        roman += symbols[10] * (digit // 10)
                elif digit < 100:
                    if digit == 90:
                        roman += symbols[10] + symbols[100]
                    else:
                        roman += symbols[50] + symbols[10] * ((digit - 50) // 10)
                elif digit < 500:
                    if digit == 400:
                        roman += symbols[100] + symbols[500]
                    else:
                        roman += symbols[100] * (digit // 100)
                elif digit < 1000:
                    if digit == 900:
                        roman += symbols[100] + symbols[1000]
                    else:
                        roman += symbols[500] + symbols[100] * ((digit - 500) // 100)
                else:
                    roman += symbols[1000] * (digit // 1000)
        return roman

solution = Solution().intToRoman(1994)
print(solution)

# It was quite a messy and rough solution
# but it's the fastest way to solve this problem
# I'll try to find a better solution later

# I wanted to save time, so, I just used AI to list all the if else cases
# https://leetcode.com/problems/integer-to-roman/submissions/962549026/