class Solution {
public:
    bool check(unordered_map<char, int>& f1, unordered_map<char, int>& f2){
        for (auto& [ch, f] : f2){
            if (f1[ch] != f) return false;
        }
        return true;
    }
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> freq1, freq2;
        for (auto& ch : s1){
            freq1[ch]++;
        }
        for (int i=0; i<s1.size(); i++){
            freq2[s2[i]]++;
        }
        if (check(freq2, freq1)) return true;
        for (int i=s1.size(); i<s2.size(); i++){
            freq2[s2[i - s1.size()]]--;
            freq2[s2[i]]++;
            if (check(freq2, freq1)) return true;
        }
        return false;
    }
};
