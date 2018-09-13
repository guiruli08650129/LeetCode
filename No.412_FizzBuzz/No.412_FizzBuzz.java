class Solution {
    public List<String> fizzBuzz(int n) {
        int i = 0;
        List<String> ans = new LinkedList<String>();
        while(i<n)
        {
            if((i+1)%15==0)
                ans.add("FizzBuzz");
            else if((i+1)%5==0)
                ans.add("Buzz");
            else if((i+1)%3==0)
                ans.add("Fizz");
            else
                ans.add(Integer.toString((i+1)));
            i+=1;
        }
        return ans;
    }
}