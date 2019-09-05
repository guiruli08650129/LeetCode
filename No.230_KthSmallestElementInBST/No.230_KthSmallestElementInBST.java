/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    Stack<TreeNode> s = new Stack<TreeNode>();
    public int kthSmallest(TreeNode root, int k) {
        
        if(root == null)
            return 0;
        
        pushLeft(root);        
        
        while(!s.empty())
        {
            TreeNode n = s.pop();
            if(--k == 0)
                return n.val;
            if(n.right != null)
                pushLeft(n.right);
        }
        
        return 0;
        
    }
    private void pushLeft(TreeNode node)
    {
        TreeNode current = node;
        while(current != null)
        {
            s.push(current);
            current = current.left;
        }
    }
}