class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        nums = []
        i = 0
        s += "random_string"
        while i<len(s)-1:
            if (s[i] + s[i+1]).isdigit():
                nums.append(int(s[i] + s[i+1]))
                i += 2
            elif s[i].isdigit():
                nums.append(int(s[i]))
                i += 1
            else:
                i+=1
        sorted_nums = sorted(nums)
        new_nums = []
        for i in sorted_nums:
            if i not in new_nums:
                new_nums.append(i)
        if new_nums != nums:
            return False
        if sorted_nums == nums:
            return True
        return False

solution = Solution()
print(solution.areNumbersAscending("hello world 5 x 5"))

# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/submissions/941097463/