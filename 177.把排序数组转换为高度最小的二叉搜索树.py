#给一个排序数组（从小到大），将其转换为一棵高度最小的排序二叉树。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def buildTree(self, nums, start, end):
        if start > end:
            return
        mid = (start + end) / 2
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums, start, mid - 1)
        root.right = self.buildTree(nums, mid + 1, end)
        return root
    
    def sortedArrayToBST(self, A):
        if A is None:
            return
        return self.buildTree(A, 0, len(A) - 1)
