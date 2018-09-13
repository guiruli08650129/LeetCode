class Solution {
    public void moveZeroes(int[] nums) {
        
        for(int i = 0 ; i < nums.length ; i++)
        {
            int id = i;
            while(nums[i]==0 && (id+1)!= nums.length)
            {
                int temp = nums[id+1];
                nums[id+1] = nums[i];
                nums[i] = temp;
                id += 1;
            }
            
        }
        
    }
}