#include <iostream>
#include <vector>
#include "two_sum.cpp"

using namespace std;

int main() {
    vector<int> nums = {3, 3};
    for (int num : TwoSum::twoSum(nums, 6))
        cout << num << endl;
    return 0;
}