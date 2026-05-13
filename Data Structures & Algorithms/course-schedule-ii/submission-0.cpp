class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> graph;
        unordered_map<int, int> inDegree;
        for (int i=0; i<numCourses; i++){
            inDegree[i] = 0;
        }
        for (auto& mapping : prerequisites){
            graph[mapping[1]].push_back(mapping[0]);
            inDegree[mapping[0]]++;
        }
        queue<int> q;
        for (int i=0; i<numCourses; i++){
            if (inDegree[i] == 0){
                q.push(i);
            }
        }
        vector<int> order;
        while(!q.empty()){
            auto current = q.front();
            order.push_back(current);
            q.pop();
            for (auto& dep : graph[current]){
                inDegree[dep]--;
                if (inDegree[dep] == 0){
                    q.push(dep);
                }
            }
        }
        return order.size() == numCourses ? order : vector<int>();
    }
};
