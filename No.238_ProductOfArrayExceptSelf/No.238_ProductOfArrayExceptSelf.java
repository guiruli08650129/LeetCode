class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        int[] ans = new int[nums.length];
        
        left[0] = 1;        
        right[nums.length-1] = 1;
        
        for(int i = 1 ; i < left.length ; i++)
            left[i] = nums[i-1] * left[i-1];
        
        for(int j = right.length-2 ; j >= 0 ; j--)
            right[j] = nums[j+1] * right[j+1];        
        
        for(int k = 0 ; k < ans.length ; k++)
            ans[k] = left[k] * right[k];
        
        return ans;
    }
}