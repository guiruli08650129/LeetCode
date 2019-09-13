class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 1
        for i in nums:
            if i <= 0:
                continue            
            if ans == i:
                ans += 1            
        
        return ans