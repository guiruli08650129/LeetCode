class Solution:
    def fac(self, f):
        ans = 1
        for i in range(1, f):
            ans = ans * i
        return ans        
    
    def uniquePaths(self, m: int, n: int) -> int:
        return (int)(self.fac(m+n-1)/(self.fac(m)*self.fac(n)))