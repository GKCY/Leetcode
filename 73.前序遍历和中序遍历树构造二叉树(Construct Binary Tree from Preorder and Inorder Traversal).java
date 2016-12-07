//根据前序遍历和中序遍历树构造二叉树.

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
 
 
public class Solution {
    /**
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
    private int findPosition(int[] arr, int start, int end, int key){
        int i;
        for (i = start; i <= end; i++){
            if(arr[i] == key)
                return i;
        }
        return -1;
    }
    
    private TreeNode myBuildTree (int[] inorder, int instart, int inend, int[] preorder, int prestart, int preend){
        if(instart > inend)
            return null;
        int position = findPosition(inorder, instart, inend, preorder[prestart]);
        TreeNode root = new TreeNode(preorder[prestart]);
        root.left = myBuildTree(inorder, instart, position-1, preorder,prestart+1, prestart+position-instart);
        root.right = myBuildTree(inorder, position+1, inend, preorder, position - inend + preend + 1, preend);
        return root;
    }
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // write your code here
        if (preorder.length != inorder.length)
            return null;
        return myBuildTree(inorder, 0, inorder.length-1, preorder, 0, preorder.length-1);
    }
}
