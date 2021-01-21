class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        num = int(len(piles) / 3)
        ans = 0

        for i in range(num):
            ans += piles[i * 2 + 1]
        return ans
