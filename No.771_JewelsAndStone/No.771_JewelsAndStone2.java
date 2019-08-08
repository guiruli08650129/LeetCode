class Solution {
    public int numJewelsInStones(String J, String S) {
        
        int count = 0;
        for(int i = 0 ; i < S.length() ; i++)
        {
            String s = Character.toString(S.charAt(i));
            if(J.contains(s))
                count++;
        }
        
        return count;
    }
}