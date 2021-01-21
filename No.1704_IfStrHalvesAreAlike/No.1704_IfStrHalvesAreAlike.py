class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:int(len(s) / 2)]
        b = s[int(len(s) / 2):]

        a_sum = 0
        for i in ['a', 'e', 'i', 'o', 'u']:
            a_sum += a.lower().count(i)
        b_sum = 0
        for i in ['a', 'e', 'i', 'o', 'u']:
            b_sum += b.lower().count(i)

        return a_sum == b_sum
