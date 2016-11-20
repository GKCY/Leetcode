#二叉查找树按照中序遍历的时候是递增的，用一个lastVal记录上个值，如果出现递减，就不是查找树
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
        self.isBST = True
        self.lastVal = None
        self.validate(root)
        return self.isBST
        
    def validate(self, root):
        if root is None:
            return 
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)
