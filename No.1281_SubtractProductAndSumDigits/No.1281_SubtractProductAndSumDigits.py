class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        n2 = list(str(n))
        for digit in n2:
            p = p * int(digit)
            s = s + int(digit)

        return p - s
