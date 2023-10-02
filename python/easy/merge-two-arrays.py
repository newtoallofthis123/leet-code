# https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num1 = nums1[:m]
        num2 = nums2[:n]
        temp = []
        i=j=0
        while i<len(num1) and j<len(num2):
            if num1[i] < num2[j]:
                temp.append(num1[i])
                i += 1
            else:
                temp.append(num2[j])
                j += 1
        while i<len(num1):
            temp.append(num1[i])
            i+=1
        while j<len(num2):
            temp.append(num2[j])
            j+=1
        k = 0
        while k<len(temp):
            nums1[k] = temp[k] 
            k += 1
            

solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m=n=3
solution.merge(nums1, m, nums2, n)
print(nums1)

# Not proud of how messy this implementation is
# https://leetcode.com/problems/merge-sorted-array/submissions/941085488/