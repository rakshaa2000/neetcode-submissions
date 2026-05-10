#include <string>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty() || s.length() < t.length()) {
            return "";
        }
        vector<int> freqT(128, 0);
        for (char c : t) {
            freqT[c]++;
        }

        int start = 0, end = 0;
        int minLen = INT_MAX;
        int minStart = 0;
        int required = t.length(); 

        while (end < s.length()) {
            if (freqT[s[end]] > 0) {
                required--;
            }
            freqT[s[end]]--;
            end++;
            while (required == 0) {
                if (end - start < minLen) {
                    minLen = end - start;
                    minStart = start;
                }
                freqT[s[start]]++;
                if (freqT[s[start]] > 0) {
                    required++;
                }
                start++;
            }
        }

        return minLen == INT_MAX ? "" : s.substr(minStart, minLen);
    }
};