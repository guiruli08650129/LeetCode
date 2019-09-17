class Solution:
    def uniquePaths(self, m: int, n: int) -> int:        
        if not m or not n:
            return 0
        
        per = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                per[j] += per[j-1]
        return per[-1]