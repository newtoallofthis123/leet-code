#include "iostream"

using namespace std;

class Solution {
private:
    static bool isPalindrome(string &str) {
        size_t len = str.length();
        for (int i = 0; i < len / 2; i++) {
            if (str[i] != str[len - i - 1]) {
                return false;
            }
        }
        return true;
    }

public:
    static string longestPalindrome(string s) {
        size_t len = s.length();
        string arr[len];

        for (int i = 0; i < len; i++) {
            string str;
            for (int j = i; j < len; j++) {
                str += s[j];
                if (isPalindrome(str)) {
                    arr[i] = str;
                }
            }
        }

        string max;

        for (int i = 0; i < len; i++) {
            if (arr[i].length() > max.length()) {
                max = arr[i];
            }
        }
        return max;
    }
};