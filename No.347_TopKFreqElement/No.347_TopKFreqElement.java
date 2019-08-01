class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> dict = new HashMap<Integer, Integer>();
        
        for(int i = 0 ; i < nums.length ; i++)
        {
            int keyNum = nums[i];
            if(dict.containsKey(keyNum))
                dict.put(keyNum, dict.get(keyNum) + 1);
            else
                dict.put(keyNum, 1);
        }
        
        List<Map.Entry> entryList = new ArrayList<>(dict.entrySet());
        Comparator<Map.Entry> sortbyvalue = (e1, e2)->{return ((Integer)e2.getValue()).compareTo((Integer)e1.getValue()); };
        Collections.sort(entryList, sortbyvalue);
        
        LinkedList<Integer> answer = new LinkedList<Integer>();
        for(Map.Entry e: entryList)
        {
            answer.add((Integer)e.getKey());
            if(answer.size() == k)
                break;
        }
        return answer;        
    }
}