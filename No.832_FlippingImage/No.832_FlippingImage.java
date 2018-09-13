class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int[][] B = new int[A.length][A.length];
    	for(int i = 0 ; i < A.length ; i++)
        {
        	for(int j = 0 ; j < A[i].length ; j++)
        	{
        		B[i][A.length-1-j] = A[i][j]^1;
        	}
        }
    	return B;
    }
}