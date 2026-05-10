class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (auto& current : strs){
            vector<int> chars(26, 0);
            for (auto& ch : current){
                chars[ch - 'a']++;
            }
            string bitmask = "";
            for(auto& num : chars){
                bitmask += "." + to_string(num);
            }
            groups[bitmask].push_back(current);
        }
        vector<vector<string>> answer;
        for (auto& [key, group] : groups){
            answer.push_back(group);
        }
        return answer;
    }
};
