class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mapToIndex;
        for (int i=0; i<nums.size(); i++){
            if (mapToIndex.count(target - nums[i])){
                return {mapToIndex[target - nums[i]], i};
            }
            mapToIndex[nums[i]] = i;
        }
        return {-1, -1};
    }
};
