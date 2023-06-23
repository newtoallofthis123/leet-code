from itertools import combinations

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combis = list(combinations(candidates, 3))
        return [i for i in combis if sum(i) == target]
    
solution = Solution().combinationSum([2,3,6,7], 7)
print(solution)