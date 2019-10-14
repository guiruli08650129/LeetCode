class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = s.strip()
        if ss:
            string = ss.split(" ")
            return len(string[-1])
        else:
            return 0