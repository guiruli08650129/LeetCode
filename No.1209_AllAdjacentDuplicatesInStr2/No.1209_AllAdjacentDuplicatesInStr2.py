class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        begin = 1
        while begin:
            begin, ix, count = 0, 0, 1
            while ix < len(s) - 1:
                ix += 1
                if s[ix] == s[ix - 1]:
                    count += 1
                else:
                    count = 1
                if count == k:
                    s = s[:ix - k + 1] + s[ix + 1:]
                    begin = 1
                    ix = max(0, ix - k)
                    count = 1

        return s
                