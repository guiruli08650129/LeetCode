class Solution {
    public int numJewelsInStones(String J, String S) {
        Set map = new HashSet();
        for(char c : J.toCharArray())
            map.add(c);
        
        int count = 0;
        for(char s : S.toCharArray())
        {
            if(map.contains(s))
                count++;
        }
        
        return count;
    }
}