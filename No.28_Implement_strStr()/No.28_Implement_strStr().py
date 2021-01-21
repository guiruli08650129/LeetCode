class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return 0
        ans = haystack.find(needle)
        return ans
