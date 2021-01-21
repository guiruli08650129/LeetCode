class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary = 0
        secondary = 0
        for i in range(len(mat)):
            primary += mat[i][i]
            secondary += mat[len(mat) - i - 1][i]

        if len(mat) % 2 == 1:
            return primary + secondary - mat[int((len(mat) + 1) / 2) - 1][int((len(mat) + 1) / 2) - 1]
        else:
            return primary + secondary
