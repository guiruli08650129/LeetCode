class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]] = 1
            else:
                d[nums[i]] = d[nums[i]] + 1

        ans = 0
        for j in d.keys():
            if d[j] > 1:
                ans += int(d[j] * (d[j] - 1) / 2)
        return ans
