class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d.keys():
                d[groupSizes[i]] = [i]
            else:
                d.get(groupSizes[i]).append(i)

        ans = []
        for k, v in d.items():
            if len(v) <= k:
                ans.append(v)
            else:
                for j in range(int(len(v) / k)):
                    ans.append(v[j * k:(j + 1) * k])
        return ans
