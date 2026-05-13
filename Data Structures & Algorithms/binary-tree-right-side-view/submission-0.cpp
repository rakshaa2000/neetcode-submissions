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
    vector<int> rightSideView(TreeNode* root) {
        queue<TreeNode*> q;
        vector<int> vals;
        if (!root) return {};
        q.push(root);
        while (!q.empty()){
            int size = q.size();
            int right = 0;
            for (int i=0; i<size; i++){
                auto front = q.front();
                q.pop();
                if (front->left) q.push(front->left);
                if (front->right) q.push(front->right);
                right = front->val;
            }
            vals.push_back(right);
        }
        return vals;
    }
};
