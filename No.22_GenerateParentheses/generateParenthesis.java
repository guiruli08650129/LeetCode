class Solution {
	public List<String> generateParenthesis(int n){
        List<String> ans = new ArrayList();
        recursive(ans, "", 0, 0, n);
        return ans;
        
    }
	private void recursive(List<String> ans, String s, int left, int right, int n) {
		if (s.length()==2*n)
		{
			ans.add(s);
			return;
		}
		if (left<n)
			recursive(ans, s+"(", left+1, right, n);
		if (right<left)
			recursive(ans, s+")", left, right+1, n);
	}
}