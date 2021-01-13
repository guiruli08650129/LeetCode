class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        previous = nums[0]
        for i in range(1, len(nums)):
            previous = previous + nums[i]
            ans.append(previous)
        return ans
