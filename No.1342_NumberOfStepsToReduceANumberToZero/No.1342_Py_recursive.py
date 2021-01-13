class Solution:
    def numberOfSteps(self, num: int) -> int:
        def recursive(num, step):
            if num == 2:
                return step + 2
            elif num == 1:
                return step + 1
            else:
                if num % 2 == 0:
                    return recursive(num / 2, step + 1)
                else:
                    return recursive(num - 1, step + 1)

        step = 0
        step = recursive(num, 0)
        return step
