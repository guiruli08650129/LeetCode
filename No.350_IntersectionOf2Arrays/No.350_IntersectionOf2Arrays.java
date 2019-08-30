class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        HashMap  h1 = collectNums(nums1);
        HashMap  h2 = collectNums(nums2);

        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(Object key : h1.keySet())
        {
            if(h2.containsKey(key))
            {
                int inter = ((int)h1.get(key) > (int)h2.get(key)) ? (int)h2.get(key) : (int)h1.get(key);
                for(int j = 0 ; j < inter ; j++)
                    arr.add((int)key);
            }
        }
        
        int[] ans = new int[arr.size()];
        for(int a = 0 ; a < arr.size() ; a++)
            ans[a] = arr.get(a);
            
        return ans;
        
    }
    private HashMap  collectNums(int[] nums)
    {
        HashMap h = new HashMap ();
        for(int n : nums)
        {
            if(h.containsKey(n))
            {
                int count = (int)h.get(n) + 1;
                h.put(n, count);
            }
            else
                h.put(n, 1);
        }
        return h;
    }
}