class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prodLeft(nums.size(), 1), prodRight(nums.size(), 1);
        for (int i=1; i<nums.size(); i++){
            prodLeft[i] = prodLeft[i-1] * nums[i-1];
        }
        for (int i=nums.size()-2; i>=0; i--){
            prodRight[i] = prodRight[i+1] * nums[i+1];
        }
        for (int i=0; i<nums.size(); i++){
            prodRight[i] *= prodLeft[i];
        }
        return prodRight;
    }
};
