class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            row_min = min(matrix[i])
            ix = matrix[i].index(row_min)
            col = []
            for j in range(len(matrix)):
                col.append(matrix[j][ix])
            if row_min == max(col):
                ans.append(row_min)

        return ans
