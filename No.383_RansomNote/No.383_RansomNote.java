class Solution {
	public boolean canConstruct(String ransomNote, String magazine) {

		if (ransomNote.length() == 0)
			return true;

		StringBuilder mag = new StringBuilder(magazine);
		for (char c : ransomNote.toCharArray()) {
			int temp = mag.indexOf(String.valueOf(c));
			if (temp >= 0)
				mag.deleteCharAt(temp);
			else
				return false;
		}
		return true;
	}
}