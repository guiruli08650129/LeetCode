class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        ans = ""
        while i < len(command):
            if command[i] == "G":
                ans = ans + "G"
                i += 1
            elif command[i] == "(":
                i += 1
                if command[i] == "a":
                    ans += "al"
                    i += 3
                else:
                    ans += "o"
                    i += 1
        return ans
