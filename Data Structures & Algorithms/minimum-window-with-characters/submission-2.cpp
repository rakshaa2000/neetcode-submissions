class Solution {
public:
    bool check(unordered_map<char, int> f1, unordered_map<char, int> f2){
        for (auto& [ch , f]: f1){
            if (!f2.count(ch) || f2[ch] < f) return false;
        }
        return true;
    }
    string minWindow(string s, string t) {
        int start = 0, end = 0;
        unordered_map<char, int> freqS, freqT;
        for (auto& ch : t){
            freqT[ch]++;
        }
        int minLen = INT_MAX;
        int minStart = INT_MAX;
        while (end < s.size()){
            freqS[s[end]]++;
            while (start <= end && check(freqT, freqS)){
                if (end - start + 1 < minLen){
                    minLen = min(minLen, end - start + 1);
                    minStart = start;
                }
                freqS[s[start]]--;
                start++;
            }
            end++;
        }
        return minLen == INT_MAX ? "" : s.substr(minStart, minLen);
    }
};
