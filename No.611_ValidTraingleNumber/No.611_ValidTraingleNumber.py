class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return 0
        
        nums.sort()
        ans = 0
        for i in range(0, len(nums)-2):
            k = i+2
            for j in range(i+1, len(nums)-1):
                if nums[i] == 0:
                    continue
                while k < len(nums) and (nums[i]+nums[j] > nums[k]):
                    k += 1
                ans += k-j-1
        
        return ans