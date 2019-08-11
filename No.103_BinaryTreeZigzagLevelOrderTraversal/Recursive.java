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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
                
        if(root == null)
            return new ArrayList<List<Integer>>();
        
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        int l = 0;
        Queue<TreeNode> record = new LinkedList<TreeNode>();
        record.add(root);
        
        while(!record.isEmpty())
        {
            int size = record.size();
            List<Integer> level = new LinkedList<Integer>();
            
            for(int i = 0 ; i < size ; i++)
            {
                TreeNode temp = record.poll();
                if(temp != null)
                {
                    level.add(temp.val);
                    record.add(temp.left);
                    record.add(temp.right);
                }
            }
            if(!level.isEmpty())
            {
                if(l % 2  != 0)
                    Collections.reverse(level);
                ans.add(level);
            }
            l++;
        }
        
        return ans;         
    }
}