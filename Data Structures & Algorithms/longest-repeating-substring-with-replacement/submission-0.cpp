class Solution {
public:
    int characterReplacement(string s, int k) {
        int maxFreq = 0, start = 0, end = 0, maxLen = 0;
        unordered_map<int, int> freq;
        while (end < s.size()){
            char ch = s[end];
            freq[ch]++;
            maxFreq = max(maxFreq, freq[ch]);
            while (start < end && end - maxFreq - start + 1 > k){
                freq[s[start]]--;
                start++;
            }
            maxLen = max(maxLen, end - start + 1);
            end++;
        }
        return maxLen;
    }
};