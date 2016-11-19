#Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

#The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return
        if root is A or root is B:
            return root
            
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        
        if left is not None and right is not None:
            return root
        if left:
            return left
        if right:
            return right
        return None
