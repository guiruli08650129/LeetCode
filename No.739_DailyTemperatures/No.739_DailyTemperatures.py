class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = []
        for i in range(len(T)):
            day = 0
            control = False
            for j in range(i + 1, len(T)):
                if T[j] > T[i]:
                    day += 1
                    control = True
                    break
                else:
                    day += 1
            if control:
                ans.append(day)
            else:
                ans.append(0)
        return ans
