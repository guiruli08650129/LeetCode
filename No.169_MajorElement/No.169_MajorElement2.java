class Solution {
    public int majorityElement(int[] nums) {
        int ans = 0;
        Integer candidate = null;
        
        for(int n : nums)
        {
            if(ans == 0)
                candidate = n;
            ans += (n == candidate) ? 1 : -1;
        }
        
        return candidate;
    }
}