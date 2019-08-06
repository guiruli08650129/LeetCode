class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(nums, target, check):
            left = 0
            right = len(nums)

            while(left<right):
                c = (left+right) // 2
                if (nums[c] > target) or (nums[c] == target and check):
                    right = c
                else:
                    left = c+1

            return left
        
        def search(nums, target):
            left_ix = find(nums, target, True)
            
            if left_ix == len(nums) or nums[left_ix] != target:
                return [-1,-1]
            
            return [left_ix, find(nums, target, False)-1]
        
        return search(nums, target)