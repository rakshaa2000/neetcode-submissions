/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        if (!root) return {};
        q.push(root);
        vector<vector<int>> levels;
        while (!q.empty()){
            vector<int> level;
            int size = q.size();
            for (int i=0; i<size; i++){
                auto top = q.front();
                level.push_back(top->val);
                q.pop();
                if (top->left) q.push(top->left);
                if (top->right) q.push(top->right);
            }
            levels.push_back(level);
        }
        return levels;
    }
};
