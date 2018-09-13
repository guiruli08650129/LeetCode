class Solution {
	public int hammingDistance(int x, int y) {

		int ans = 0;
		String s = Integer.toBinaryString(x ^ y);
		for (char c : s.toCharArray())
			if (c == '1')
				ans++;

		return ans;
	}
}