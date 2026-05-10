class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> days;
        vector<int> inc(temperatures.size());
        for (int i=temperatures.size()-1; i>=0; i--){
            while (!days.empty() && temperatures[days.top()] <= temperatures[i]){
                days.pop();
            }
            inc[i] = days.empty() ? 0 : days.top() - i;
            days.push(i);
        }
        return inc;
    }
};
