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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();     
        if (root == null)
            return ans;        
        
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        
        while(!q.isEmpty())
        {
            int num = q.size();
            List<Integer> sublist = new ArrayList<>(num);
            
            for(int i = 0 ; i < num ; i++)
            {
                TreeNode c = q.poll();
                sublist.add(c.val);
                if(c.left != null)
                    q.add(c.left);
                if(c.right != null)
                    q.add(c.right);
            }
            
            ans.add(sublist);         
        }
        return ans;        
    }
}