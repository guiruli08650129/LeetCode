class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recursive(s='', left = 0, right = 0):
            if len(s) == n*2:
                ans.append(s)
                return
            if left < n:
                recursive(s+'(', left+1, right)
            if right < left:
                recursive(s+')', left, right+1)
                
        recursive()
        return ans