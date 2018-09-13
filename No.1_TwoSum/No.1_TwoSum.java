class Solution {
	public int[] twoSum(int[] nums, int target) {
    	int[] result = new int[2];
    	for(int j = nums.length-1 ; j >= 0 ; j--)
        {
        	for(int k = 0 ; k < j ; k++)
    		{
    			if(nums[j]+nums[k]==target)
    			{
    				result[0] = k;
    				result[1] = j;
    			}
    		}
        }
        return result;
    }
}