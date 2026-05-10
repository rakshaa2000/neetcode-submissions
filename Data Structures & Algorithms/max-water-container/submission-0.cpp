class Solution {
public:
    int maxArea(vector<int>& heights) {
        int start = 0, end = heights.size()-1;
        int largest = 0;
        while (start < end){
            largest = max(largest, (end - start) * min(heights[start], heights[end]));
            if (heights[start] < heights[end]) start++;
            else end--;
        }
        return largest;
    }
};
