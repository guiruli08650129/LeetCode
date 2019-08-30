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
    public TreeNode sortedArrayToBST(int[] nums) {
        return buildTree(nums, 0, nums.length);
    }
    private TreeNode buildTree(int[] nums, int left, int right)
    {
        TreeNode root = null;
        
        if(left < right)
        {
            int mid = left + (right - left) / 2;
            root = new TreeNode(nums[mid]);

            root.left = buildTree(nums, left, mid);
            root.right = buildTree(nums, mid+1, right);
        }
        
        return root;
    }
    
}