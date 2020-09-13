def quick(nums, lptr, rptr):

    if lptr >= rptr:
        return

    l = lptr
    r = rptr
    key = nums[lptr]
    
    while r != l:
        while nums[r]>key and l<r:
            r=r-1
        while nums[l]<=key and l<r:
            l=l+1

        if l<r:
            nums[r], nums[l] = nums[l], nums[r]

    nums[lptr] = nums[l]
    nums[l] = key
    quick(nums,lptr, l-1)
    quick(nums,l+1, rptr)

class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        quick(nums, 0, len(nums)-1)
        return nums
        
        

            
