"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    
    def binaryTreePaths(self, root):
        def find(root, path, result):
            if path == '':
                path = str(root.val)
            else:
                path = path + '->'+ str(root.val)
            if root.left:
                find(root.left, path, result)
            if root.right:
                find(root.right, path, result)
            if root.right == None and root.left == None:
                result.append(path)
        # Write your code here
        res = []
        path = ''
        if root:
            find(root, path, res)
        return res
    
