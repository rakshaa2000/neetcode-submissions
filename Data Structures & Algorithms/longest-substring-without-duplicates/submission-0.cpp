class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> freq;
        int start = 0, end = 0, maxLen = 0;
        while (end < s.size()){
            freq[s[end]]++;
            while (start < end && freq[s[end]] > 1){
                freq[s[start]]--;
                start++;
            }
            maxLen = max(maxLen, end - start + 1);
            end++;
        }
        return maxLen;
    }
};
