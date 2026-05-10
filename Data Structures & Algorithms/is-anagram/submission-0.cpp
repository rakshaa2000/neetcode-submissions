class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> frequency;
        for (auto& ch : s){
            frequency[ch]++;
        }
        for (auto& ch : t){
            frequency[ch]--;
        }
        for (auto& [ch, freq] : frequency){
            if (freq != 0) return false;
        }
        return true;
    }
};
