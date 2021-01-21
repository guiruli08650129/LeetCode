class Solution:
    def maximum69Number(self, num: int) -> int:
        cand = list(str(num))
        for i in range(len(cand)):
            if cand[i] == "6":
                cand[i] = "9"
                break
        return ''.join(cand)
