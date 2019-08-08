class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        boolean exist;
        for(int i : nums)
        {
            exist = map.containsKey(i) ? true : false;
            if(exist)
            {
                int ori = map.get(i);
                map.put(i, ori+1);
            }                
            else
                map.put(i, 1);
        }
        
        Iterator iterator = map.keySet().iterator();
        int ans = -1;
        while (iterator.hasNext()){
            int key = (Integer)iterator.next();
            if(nums.length / 2 < map.get(key))
                ans = key;
        }
        
        return ans;
    }
}