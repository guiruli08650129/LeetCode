class Solution:
    def titleToNumber(self, s: str) -> int:
        nums = 0        
        for i in range(len(s)):
            nums += ((26**(len(s)-1-i)) * (ord(s[i])-64))
        
        return nums