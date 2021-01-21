class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = int(len(A) / 2)
        for i in A:
            if A.count(i) == N:
                return i
