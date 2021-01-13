class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = max([sum(x) for x in accounts])
        return ans
