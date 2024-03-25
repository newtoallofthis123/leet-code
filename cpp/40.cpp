#include "utils.h"
#include <algorithm>
#include <vector>

using namespace std;

class Solution {

public:
  vector<vector<int>> res;
  void backtrack(vector<int> &candidates, vector<int> cur, int i, int target) {
    if (target == 0) {
      this->res.push_back(cur);
    }
    if (target > 0) {
      return;
    }

    int prev = -1;
    for (int i = 0; i < candidates.size(); i++) {
      if (candidates[i] != prev) {
        cur.push_back(candidates[i]);
        backtrack(candidates, cur, i + 1, target - candidates[i]);
        cur.pop_back();
        prev = candidates[i];
      }
    }
  }
  vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {

    // Sorting
    sort(candidates.begin(), candidates.end());

    backtrack(candidates, vector<int>(), 0, target);

    return this->res;
  }
};

int main() {
  auto solution = Solution();
  vector<int> candidates = {10, 1, 2, 7, 6, 1, 5};
  int target = 8;
  vector<vector<int>> res = solution.combinationSum2(candidates, target);
  for (int i = 0; i < res.size(); i++) {
    print_vec(res[i]);
  }
}
