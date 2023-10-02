# https://leetcode.com/problems/detonate-the-maximum-bombs/
import math

class Solution(object):
    def is_in_area(self, bomb1, bomb2):
        x1, y1, r1 = bomb1
        x2, y2, r2 = bomb2
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return distance <= r1

    def detonate_bombs(self, bombs, index, detonated):
        detonated[index] = True
        for i in range(len(bombs)):
            if not detonated[i] and self.is_in_area(bombs[index], bombs[i]):
                self.detonate_bombs(bombs, i, detonated)

    def maximumDetonation(self, bombs):
        max_detonation = 0
        for i in range(len(bombs)):
            detonated = [False] * len(bombs)
            self.detonate_bombs(bombs, i, detonated)
            detonation_count = sum(detonated)
            max_detonation = max(max_detonation, detonation_count)
        return max_detonation


bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
solution = Solution().maximumDetonation(bombs)
print(solution)

# Can I be proud of this? Yes. I can.
# Just used 

# https://leetcode.com/problems/detonate-the-maximum-bombs/submissions/962475811/
