class Solution {
    public int singleNonDuplicate(int[] nums) {
        
        if(nums.length==1)
            return nums[0];
        
        int ans = findInt(nums, 0, nums.length-1);
        return ans;
        
    }
    private int findInt(int[] arr, int left, int right)
    {
        int mid = (right+left+1)/2;

        if(arr[mid]!=arr[mid-1] && arr[mid]!=arr[mid+1])
        	return arr[mid];
        
        if(right-left+1 == 3)
        {
            return arr[left]==arr[mid]? arr[mid+1]:arr[mid-1];
        }        
        
        if((mid)%2==0)
        {
            if(arr[mid]==arr[mid-1])
                return findInt(arr, left, mid);
            if(arr[mid]==arr[mid+1])
                return findInt(arr, mid, right);
        }
        
        if((mid)%2==1)
        {
            if(arr[mid]==arr[mid-1])
                return findInt(arr, mid+1, right);
            if(arr[mid]==arr[mid+1])
                return findInt(arr, left, mid-1);
        }
        
        return 0;
    }
}