class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = 0
        for item in nums:
            check ^= item
        return check