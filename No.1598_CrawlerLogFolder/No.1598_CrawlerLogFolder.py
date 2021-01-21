class Solution:
    def minOperations(self, logs: List[str]) -> int:
        def operations(step, level):
            if step == "../":
                return 0 if level == 0 else (level - 1)
            elif step == "./":
                return level
            else:
                return level + 1

        j = 0
        while j in range(len(logs)):
            if logs[j] == "../" or logs[j] == "./":
                j += 1
            else:
                break

        level = 0
        for i in range(j, len(logs)):
            level = operations(logs[i], level)

        if level < 0:
            return 0
        return level
