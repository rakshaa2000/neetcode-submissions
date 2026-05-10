class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> maxHeap;
        vector<int> output;
        for (int i=0; i<nums.size(); i++){
            maxHeap.push({nums[i], i});
            if (i >= k-1){
                while (!maxHeap.empty() && maxHeap.top().second <= i-k){
                    maxHeap.pop();
                }
                output.push_back(maxHeap.top().first);
            }
        }
        return output;
    }
};
