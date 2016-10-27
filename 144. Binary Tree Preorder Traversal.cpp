//Given a binary tree, return the preorder traversal of its nodes' values.

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        stack<TreeNode*> s;
        vector<int> nodes;
        if(!root) return nodes;
        TreeNode* temp = root;
        s.push(root);
        while(!s.empty())
        {
           temp = s.top();
           s.pop();
           nodes.push_back(temp->val);
           if(temp->right) s.push(temp->right);
           if(temp->left) s.push(temp->left);
        }
        return nodes;
    }
};
