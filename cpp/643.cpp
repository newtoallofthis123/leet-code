
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  double findMaxAverage(vector<int> &nums, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) {
      sum += nums[i];
    }
    int max_sum = sum;
    for (int i = k; i < nums.size(); i++) {
      sum += nums[i] - nums[i - k];
      max_sum = max(max_sum, sum);
    }
    return (double)max_sum / k;
  }
};

int main() {
  auto solution = Solution();
  vector<int> nums = {1, 12, -5, -6, 50, 3};
  cout << solution.findMaxAverage(nums, 4) << endl;
}
