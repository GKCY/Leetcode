#Flatten a binary tree to a fake "linked list" in pre-order traversal.

#Here we use the right pointer in TreeNode as the next pointer in ListNode.




"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def preOrder(self, root, L):
        if root is None:
            return
        L.append(root.val)
        self.preOrder(root.left, L)
        self.preOrder(root.right, L)
        
    def flatten(self, root):
        # write your code here
        L = []
        self.preOrder(root, L)
        for i in range(1, len(L)):
            tmp = TreeNode(L[i])
            root.right = tmp
            root.left = None
            root = root.right
    
