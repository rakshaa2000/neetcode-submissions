class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;
        for (int num : numSet){
            if (!numSet.count(num-1)){
                int seq = num+1;
                while (numSet.count(seq)){
                    seq++;
                }
                longest = max(longest, seq - num);
            }
        }
        return longest;
    }
};
