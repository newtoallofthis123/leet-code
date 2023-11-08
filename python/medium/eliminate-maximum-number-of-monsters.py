# V = S/t
# t = 1min

class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
      
      time_to_reach = [dist[i]/speed[i] for i in range(len(dist))]
      time_to_reach.sort()

      print(time_to_reach)
      for i in range(len(time_to_reach)):
         if time_to_reach[i] <= i:
            return i

      return len(dist)


solution = Solution()
print(solution.eliminateMaximum([1,3,4], [1,1,1]))