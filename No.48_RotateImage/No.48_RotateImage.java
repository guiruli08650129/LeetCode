class Solution {
    public void rotate(int[][] matrix) {
        
        int length = matrix.length;
        int[][] target = new int[length][matrix[0].length];
        for (int i = 0; i < length; i++) 
            System.arraycopy(matrix[i], 0, target[i], 0, matrix[i].length);       
        
        for(int i = 0 ; i < matrix.length ; i++)
        {
            for(int j = 0 ; j < matrix[0].length ; j++)
            {
                swap(matrix, i, j, target);
            }
        }
    }
    private void swap(int[][] m, int i, int j, int[][] c)
    {
        int newI = j;
        int newJ = m.length - 1 - i;        
        m[newI][newJ] = c[i][j];
        
    }
}