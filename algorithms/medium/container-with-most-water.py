# Trying to figure this out
# TODO

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 1
        heights = {}
        for i in range(len(height)):
            heights[height[i]] = i+1
        for val in heights.keys():
            for other in heights.keys():
                if min(val, other) * max(heights[val], heights[other]) > max_area:
                    max_area =  min(val, other) * max(heights[val], heights[other])
        print(heights)
        return max_area

solution = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(solution)