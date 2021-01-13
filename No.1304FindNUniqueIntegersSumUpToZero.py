class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n == 1:
            return [0]
        if n % 2 == 0:
            neg = int(n/2)
            return [-x for x in range(1,neg+1)] + [y for y in range(1,neg+1)]
        else:
            neg = int((n-1)/2)
            return [-x for x in range(1,neg+1)] + [y for y in range(1,neg+1)] + [0]
            