#include "utils.h"
#include <map>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> findDuplicates(vector<int> &nums) {
    auto data = map<int, int>();
    auto result = vector<int>();

    for (auto num : nums) {
      if (data.find(num) == data.end()) {
        data[num] = 1;
      } else {
        data[num] += 1;
      }
    }

    for (auto it = data.begin(); it != data.end(); it++) {
      if (it->second == 2) {
        result.push_back(it->first);
      }
    }

    return result;
  }
};

int main() {
  auto solution = Solution();
  auto nums = vector<int>{4, 3, 2, 7, 8, 2, 3, 1};
  print_vec(solution.findDuplicates(nums));
}
