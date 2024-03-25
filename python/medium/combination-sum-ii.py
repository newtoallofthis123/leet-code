class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
    
        result = []

        def backtrack(curr, pos, target):
            if target == 0:
                result.append(curr)
            if target < 0:
                return
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i-1]:
                    continue
                backtrack(curr + [candidates[i]], i + 1, target - candidates[i])

        backtrack([], 0, target)
        return result

solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))
