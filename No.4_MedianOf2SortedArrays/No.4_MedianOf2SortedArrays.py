class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum_idx = (len(nums1) + len(nums2))
        nums = nums1 + nums2
        nums.sort()

        if sum_idx % 2 == 1:
            mid_idx = int(sum_idx // 2) + 1 - 1
            return nums[mid_idx]
        else:
            mid_idx = int(sum_idx / 2) - 1
            return (nums[mid_idx] + nums[mid_idx + 1]) / 2
