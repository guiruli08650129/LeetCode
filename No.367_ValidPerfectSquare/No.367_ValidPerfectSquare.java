class Solution {
    public boolean isPerfectSquare(int num) {
    	int size = 0;
        while(num>= 0)
        {
        	num = num - (size*2+1);
        	if(num==0)
        		return true;
        	size++;
        }
        return false;
    }
}