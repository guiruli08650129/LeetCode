class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};
        binarySearch(ans, 0, nums.length-1, nums, target);
        return ans[0] == Integer.MAX_VALUE ? new int[]{-1, -1} : ans;        
    }
    
    public void binarySearch(int[] ans, int start, int end , int[] nums, int target){
        if(start > end) return;
        
        int mid = (start + end) / 2;
        
        if(nums[mid] == target)
        {
            ans[0] = Math.min(mid, ans[0]);
            ans[1] = Math.max(mid, ans[1]);
            binarySearch(ans, start, mid-1, nums, target);
            binarySearch(ans, mid+1, end, nums, target);
        }
        else if(nums[mid] > target)
            binarySearch(ans, start, mid-1, nums, target);
        else
            binarySearch(ans, mid+1, end, nums, target);
            
    }
}