class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 2:
            if num % 2 == 0:
                num = num / 2
                step += 1
            else:
                num = num - 1
                step += 1
        if num == 2:
            return step + 2
        elif num == 1:
            return step + 1
        else:
            return 0
