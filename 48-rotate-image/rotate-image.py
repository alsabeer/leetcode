class Solution:
    def rotate(self, matrix):
        arr = [[0] * len(matrix) for _ in range(len(matrix))]
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                arr[i][j] = matrix[n - 1 - j][i]
        matrix[:]=arr

        