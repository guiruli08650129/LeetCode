class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = nums.copy()
        sortedNums.sort()
        d = {}
        for i in sortedNums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] = d[i] + 1

        ans = []
        uniq = list(d.keys())
        uniq.sort()
        for j in nums:
            k = uniq.index(j)
            each = 0
            for m in range(0, k):
                each += d.get(uniq[m])
            ans.append(each)
        return ans
