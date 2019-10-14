class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pre = -sys.maxsize -1
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                pre = nums[i]
            else:
                return i
        return len(nums)