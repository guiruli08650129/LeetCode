class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        
        ArrayList<Integer> leftList = new ArrayList<Integer>();
        ArrayList<Integer> topList = new ArrayList<Integer>();
        for(int i = 0 ; i < grid.length ; i++)
        {
            int topMax = 0;
            int leftMax = 0;
            
            for(int j = 0 ; j < grid[0].length ; j++)
            {
                if(topMax < grid[i][j])
                   topMax = grid[i][j];
                if(leftMax < grid[j][i])
                    leftMax = grid[j][i];                                
            }
            
            topList.add(topMax);
            leftList.add(leftMax);
        }        
        
        int[][] increase = new int[grid.length][grid.length];
        for(int i = 0 ; i < topList.size() ; i++)
        {
            for(int j = 0 ; j < leftList.size() ; j++)
            {
                if(topList.get(i)>leftList.get(j))
                	increase[i][j] = leftList.get(j);
                else
                	increase[i][j] = topList.get(i);
            }
        }

        int sum = 0;
        for(int i = 0 ; i < grid.length ; i++)
            for(int j = 0 ; j < grid[0].length ; j++)
                sum+=(increase[i][j]-grid[i][j]);
        
        return sum;
    }
}