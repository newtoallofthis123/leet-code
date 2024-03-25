
#include <iostream>
using namespace std;

class Solution {
public:
  string removeStars(string s) {
    string res = "";
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '*') {
        if (res.size() > 0) {
          res.pop_back();
        }
      } else {
        res += s[i];
      }
    }

    return res;
  }
};

int main() {
  auto solution = Solution();
  cout << solution.removeStars("leet**cod*e") << endl;
}
