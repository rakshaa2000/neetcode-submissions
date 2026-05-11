class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> pairs;
        for (int i=0; i < position.size(); i++){
            pairs.push_back({position[i], speed[i]});
        }
        sort(pairs.begin(), pairs.end());
        stack<double> stack;
        for (int i=pairs.size()-1; i >= 0; i--){
            double time = (target - pairs[i].first) / (pairs[i].second * 1.0);
            if (stack.empty() || stack.top() < time){
                stack.push(time);
            }
        }
        return stack.size();
    }
};