class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i]) # 把目前的值跟(當前值+前一個數值)做比較，並取最大值
            
        return max(nums)