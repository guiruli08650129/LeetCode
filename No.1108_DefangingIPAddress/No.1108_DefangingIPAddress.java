class Solution {
    public String defangIPaddr(String address) {
        String s = "";
        char[] arr = address.toCharArray();
        
        for(char c : arr)
        {
            if(c == '.')
                s = s + "[.]";
            else
                s = s + c;
        }
        return s;
    }
}