class Solution {
    public int maxProfit(int[] prices) {
        
        if(prices.length == 0)
            return 0;        
        
        int minPrice = Integer.MAX_VALUE;
        int profit = 0;
        for(int i = 0 ; i < prices.length ; i++)
        {
            if(minPrice >= prices[i])
                minPrice = prices[i];
            else
            {
                if((prices[i] - minPrice) > profit)
                    profit = prices[i] - minPrice;
            }
        }
        return profit;
    }
}