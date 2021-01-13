class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = list(" " * len(indices))
        s2 = list(s)
        for i, j in zip(indices, s2):
            ans[i] = j
        return ''.join(ans)
