class Solution:
    def trimMean(self, arr: List[int]) -> float:
        discard = int(len(arr) * 0.05)
        arr.sort()
        cand = arr[discard:len(arr) - discard]
        return sum(cand) / len(cand)
