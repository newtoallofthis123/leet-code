
class Solution:
    def combinationSum(self, candidates,target):
        result = []
        
        if target == 0:
            result.append([])
            return result
        if target < 0:
            return None

        for candidate in candidates:
            rem = target - candidate
            if self.combinationSum(candidates, rem) != None:
                for i in self.combinationSum(candidates, rem):
                    if i != None:
                        i.append(candidate)
                        i.sort()
                        if i not in result:
                            result.append(i)
        return result

    
solution = Solution().combinationSum([2,3,6,7], 7)
print(min(solution, key=len))