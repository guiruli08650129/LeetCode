class Solution {
    public String toLowerCase(String str) {
        String s = "";
        for(int i = 0 ; i < str.length() ; i++)
        {
        	char c = str.charAt(i);
            if(c>='A'&& c<='Z')
                s += Character.toString((char) (c+32));
            else
            	s += c;
                
        }
        return s;
    }
}