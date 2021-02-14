import math

class diagonalDifference():
    def __init__(self, matrix):
        self.matrix = matrix

    def diagonal_sum(self):
        i = j = 0
        diagonal = 0
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if i == j:
                    diagonal += self.matrix[i][j]
        return diagonal

    def reverse_lines(self):
        for i in range(0, len(self.matrix)):
            self.matrix[i].reverse()

        return self.matrix

    def absolute_diference_value(self):
        main_diagonal_sum = secondary_diagonal_sum = 0
        main_diagonal_sum = self.diagonal_sum()
        self.reverse_lines()
        secondary_diagonal_sum = self.diagonal_sum()
        absolute_diference = main_diagonal_sum - secondary_diagonal_sum

        return abs(absolute_diference)