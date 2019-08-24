class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniset = set()
        for n in nums:
            if n not in uniset:
                uniset.add(n)
            else:
                return True
        return False