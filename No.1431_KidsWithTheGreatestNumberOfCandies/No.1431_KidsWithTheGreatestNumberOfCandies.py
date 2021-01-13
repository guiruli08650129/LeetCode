class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        subCand = max(candies) - extraCandies
        ans = []
        for i in candies:
            if i >= subCand:
                ans.append(True)
            else:
                ans.append(False)
        return ans
