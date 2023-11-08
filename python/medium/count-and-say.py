"""
1 -> 11 -> 21 -> 1211 -> 111221 -> 312211
"""

class Solution:
    def get_counts(self, num:str)->str:
        nums = list(num)
        nums_list = []
        i = 0
        while i<len(nums):
            tar = nums[i]
            times = 0
            while nums[i] == tar:
                times += 1
                print(i, nums[i], tar, times)
                if i == len(nums)-1:
                    nums_list.append(str(times) + tar)
                    return ''.join(nums_list)
                else:
                    i+=1
            nums_list.append(str(times) + tar)
        return ''.join(nums_list)
        
    def countAndSay(self, n: int) -> str:
        current = "1"
        if n == 1:
            return current
        nums_list = []
        for i in range(n-1):
            temp = self.get_counts(current)
            nums_list.append(temp)
            current = temp
        return nums_list[-1]

solution = Solution()
print(solution.countAndSay(4))

# https://leetcode.com/problems/count-and-say/submissions/1094372667
# Can be better optimized
