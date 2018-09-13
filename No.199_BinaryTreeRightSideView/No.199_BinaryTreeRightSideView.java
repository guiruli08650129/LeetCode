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
    public List<Integer> rightSideView(TreeNode root) {
        
        List<Integer> ans = new LinkedList<Integer>();
        if(root == null)
            return ans;
        
        Queue<TreeNode> que = new LinkedList();
        que.add(root);
        while(!que.isEmpty())
        {
            int size = que.size();
            while(size>0)
            {
                TreeNode node = que.poll();
                if(size == 1)
                    ans.add(node.val);
                if(node.left!=null)
                    que.add(node.left);
                if(node.right!=null)
                    que.add(node.right);
                size--;
            }
        }
        
        return ans;
    }
}