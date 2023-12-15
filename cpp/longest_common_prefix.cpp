#include <iostream>
#include <vector>
using namespace std;

class LongestCommonPrefix{
public:
    static string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string prefix = strs[0];

        for(const string& s : strs){
            while (s.find(prefix) != 0){
                prefix = prefix.substr(0, prefix.length() - 1);
            }
        }
        return prefix;
    }
};