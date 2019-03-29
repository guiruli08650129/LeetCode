class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        right = []

        if len(s) % 2 == 1:
            return False

        for i, word in enumerate(s, 0):
            if word == '(':
                left.append(word)
                right.append(')')
            elif word == '[':
                left.append(word)
                right.append(']')
            elif word == '{':
                left.append(word)
                right.append('}')
            if word == ')' or word == ']' or word == '}':
                if len(right) == 0:
                    return False
                else:
                    check = right.pop()
                    if check != word:
                        return False

        if len(right) != 0:
            return False
        else:
            return True
