class Solution {
    public int findDuplicate(int[] nums) {
        Set set = new HashSet();
        int find = -99;
        
        for(int i = 0 ; i < nums.length ; i++)
        {
            
            if(set.contains(nums[i]))
            {
                find = nums[i];
                break;
            }
            else
            {
                set.add(nums[i]);
            }
        }
        
        return find;
        
    }
}