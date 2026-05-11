class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> stk;
        heights.push_back(0);
        int maxArea = 0;
        for (int i=0; i<heights.size(); i++){
            while (!stk.empty() && heights[stk.top()] > heights[i]){
                int top = stk.top();
                stk.pop();
                int width = stk.empty() ? i : i - stk.top() - 1;
                int height = heights[top];
                maxArea = max(maxArea, width * height);
            }
            stk.push(i);
        }
        while (!stk.empty()){
            int width = heights.size() - stk.top();
            int height = heights[stk.top()];
            stk.pop();
            maxArea = max(maxArea, height*width);
        }
        return maxArea;
    }
};
