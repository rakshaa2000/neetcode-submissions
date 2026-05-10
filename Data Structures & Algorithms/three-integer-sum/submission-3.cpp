class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> triplets;
        int i = 0;
        for (; i<nums.size()-2; i++){
            int j = i+1, k = nums.size()-1;
            if (i > 0 && nums[i] == nums[i-1]) continue;
            while (j < k){
                if (nums[j] + nums[k] == -1 * nums[i]) {
                    triplets.push_back({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                    while (j < k && nums[j] == nums[j-1]) j++;
                    while (j < k && nums[k] == nums[k+1]) k--;
                }
                else if (nums[j] + nums[k] < -1 * nums[i]){
                    j++;
                }
                else{
                    k--;
                }
            }
        }
        return triplets;
    }
};
