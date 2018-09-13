class Solution {
    public int uniqueMorseRepresentations(String[] words) {
    	
    	String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
   	
    	
    	HashSet<String> set = new HashSet<>();
    	
        for(String word : words)
        {
        	StringBuilder s = new StringBuilder();
        	for(char c : word.toCharArray())
        	{
        		s.append(morse[c-97]);
        	}
        	set.add(s.toString());
        }
        return set.size();
    }
}
