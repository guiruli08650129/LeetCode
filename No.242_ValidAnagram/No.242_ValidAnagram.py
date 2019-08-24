class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        htable = {}
        for i in s:
            if i not in htable:
                htable[i] = 1
            else:
                htable[i] += 1
        
        for j in t:
            if j not in htable:
                return False
            else:
                htable[j] -= 1
        
        for k in htable.values():
            if k != 0:
                return False        
        
        return True