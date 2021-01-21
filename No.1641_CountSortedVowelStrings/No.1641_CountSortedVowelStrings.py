class Solution:
    def countVowelStrings(self, n: int) -> int:

        def sum_each(a):
            out = []
            for i in range(1, len(a) + 1):
                out.append(sum(a[:i]))
            return out

        if n == 1:
            return 5
        else:
            alpha = [1, 2, 3, 4, 5]
            if n == 2:
                return sum(alpha)
            else:
                for i in range(n - 2):
                    alpha = sum_each(alpha)

                return sum(alpha)
