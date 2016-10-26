//Given a binary tree, return the inorder traversal of its nodes' values.

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//递归解法
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder(root,res);
        return res;
    }
    
    void inorder(TreeNode* root,vector<int> &res)
    {
        if(!root)
            return;
        
        inorder(root->left,res);
        res.push_back(root->val);
        inorder(root->right,res);
    }
};

//迭代解法
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes;
        stack<TreeNode *> s;
        TreeNode* temp = root;
        while(temp != NULL || !s.empty())
        {
            if(temp != NULL)
            {
                s.push(temp);
                temp = temp->left;
            }
            else
            {
                temp = s.top();
                s.pop();
                nodes.push_back(temp->val);
                temp = temp->right;
            }
        }
        return nodes;
    }
};
