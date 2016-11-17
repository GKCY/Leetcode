'''
You have two every large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. Create an algorithm to 
decide if T2 is a subtree of T1.
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

#解法一
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    flag = False
    def isSametree(self, a, b):
        if a is None or b is None:
            return a == b
        return a.val == b.val and self.isSametree(a.left, b.left) and self.isSametree(a.right, b.right)
    
    def order(self, T1, T2):
        if self.isSametree(T1, T2):
            self.flag = True
            return
        if T1 is None:
            return
        self.order(T1.left, T2)
        self.order(T1.right, T2)
    
    def isSubtree(self, T1, T2):
        self.order(T1, T2)
        return self.flag
        
#不是很明白这种利用语法糖的解法为啥会比上面这种常规解法快很多
#解法二：
 
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def inter(self, T, L):
       if T is None:
           L.append('#')
           return
       L.append(str(T.val))
       self.inter(T.left, L)
       self.inter(T.right, L)
       
    def isSubtree(self, T1, T2):
        # write your code here
        l1 = []
        self.inter(T1, l1)
        l1 = ','.join(l1)
        
        l2 = []
        self.inter(T2, l2)
        l2 = ','.join(l2)
        
        return l1.find(l2) != -1

 
