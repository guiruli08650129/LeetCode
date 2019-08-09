class Solution {
    public boolean isHappy(int n) {        
        if(n <= 0)
            return false;
        
        while(n >= 10)
        {
            int ans = 0;
            while(n != 0)
            {
                ans += (n % 10) * (n % 10);
                n /= 10;
            }
            n = ans;            
        }
        
        return n == 1 || n == 7;
    }
}