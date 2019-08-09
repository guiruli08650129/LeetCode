class Solution {
    public int missingNumber(int[] nums) {
        Set map = new HashSet();
        for(int i = 0 ; i < nums.length ; i++)
            map.add(nums[i]);
        
        int ans = -1;
        for(int i = 0 ; i <= nums.length ; i++)
        {
            if(map.contains(i) == false)
                ans = i;
        } 
        return ans;
    }
}