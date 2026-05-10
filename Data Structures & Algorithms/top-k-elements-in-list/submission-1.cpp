class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (auto& num : nums){
            freq[num]++;
        }
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        for (auto& [num, frequency] : freq){
            minHeap.push({frequency, num});
            if (minHeap.size() > k) minHeap.pop();
        }
        vector<int> topK;
        while (!minHeap.empty()){
            topK.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return topK;
    }
};
