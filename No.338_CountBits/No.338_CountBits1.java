class Solution {
    public int[] countBits(int num) {
        int[] count = new int[num+1];
        for(int i = 0 ; i <= num ; i++)
        {
            count[i] = Integer.bitCount(i);
        }
        return count;
    }
}