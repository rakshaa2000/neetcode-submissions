class Solution {
public:
    int trap(vector<int>& heights) {
        stack<int> monotonic;
        int water = 0;
        for (int i=0; i < heights.size(); i++){
            while (!monotonic.empty() && heights[monotonic.top()] <= heights[i]){
                int mid = heights[monotonic.top()];
                monotonic.pop();
                if (!monotonic.empty()){
                    int left = heights[monotonic.top()], right = heights[i];
                    int h = min(left, right) - mid;
                    int w = i - monotonic.top() - 1;
                    water += h * w;
                } 
            }
            monotonic.push(i);
        }
        return water;
    }
};
