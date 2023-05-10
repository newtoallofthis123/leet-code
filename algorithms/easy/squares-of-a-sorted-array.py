# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution(object):
    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr)//2]
        left = [i for i in arr if i<pivot]
        right = [i for i in arr if i>pivot]
        middle = [i for i in arr if i == pivot]

        return self.sort(left) + middle + self.sort(right)

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = [i**2 for i in nums]
        sorted_nums = self.sort(temp)
        return sorted_nums


solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))

# Could have used sorted, but wanted to use quick sort
# https://leetcode.com/problems/squares-of-a-sorted-array/submissions/941087498/