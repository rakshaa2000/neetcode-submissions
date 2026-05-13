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
    unordered_map<TreeNode*, int> cache;
    int depth(TreeNode* root){
        if (!root) return 0;
        if (cache.count(root)) return cache[root];
        return cache[root] = max(depth(root->left), depth(root->right)) + 1;
    }
    bool isBalanced(TreeNode* root) {
        if (!root) return true;
        return isBalanced(root->left) && isBalanced(root->right) && abs(depth(root->left) - depth(root->right)) <= 1;
    }
};
