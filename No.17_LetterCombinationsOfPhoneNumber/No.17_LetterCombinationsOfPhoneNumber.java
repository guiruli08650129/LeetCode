class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<String>();
        
        if(digits.length() == 0 || digits == null)
            return result;
        
        char[][] map = new char[8][];
        map[0] = "abc".toCharArray();
        map[1] = "def".toCharArray();
        map[2] = "ghi".toCharArray();
        map[3] = "jkl".toCharArray();
        map[4] = "mno".toCharArray();
        map[5] = "pqrs".toCharArray();
        map[6] = "tuv".toCharArray();
        map[7] = "wxyz".toCharArray();
        
        char[] input = digits.toCharArray();
        result.add("");
        for(char c : input)
        {
            result = expand(result, map[c-'2']);
        }
        
        return result;
    }
    private List<String> expand(List<String> ans, char[] map) 
    {
        List<String> nextstr = new ArrayList<String>();
        for(String s : ans)
            for(char c : map)
                nextstr.add(s+c);
        return nextstr;
    }
}