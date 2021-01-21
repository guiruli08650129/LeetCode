class Solution:
    def fib(self, n: int) -> int:
        def f(ix):
            if ix == 1:
                return 1
            elif ix == 0:
                return 0
            else:
                return f(ix - 1) + f(ix - 2)

        return f(n)
