# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid) == False:
                l = mid+1
            else:
                r = mid - 1
        return l


# https://leetcode.com/problems/first-bad-version/submissions/962935924/
# To be honest, I looked at the solution for this
# Why is it not fitting in my brain to use binary search or hoarse's partitioning 
# algorithm