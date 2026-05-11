class Solution {
public:
    bool searchMatrix(vector<vector<int>>& nums, int target) {
        if (target < nums[0][0] || target > nums.back().back()) return false;
        int left = 0, right = nums.size()-1;
        while (left <= right){
            int mid = left + (right - left)/2;
            if (nums[mid][0] == target) return true;
            else if (nums[mid][0] < target){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        int row = right;
        left = 0, right = nums[0].size();
        while (left <= right){
            int mid = left + (right - left)/2;
            if (nums[row][mid] == target) return true;
            else if (nums[row][mid] < target){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        return false;
    }
};
