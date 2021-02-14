from unittest import TestCase
from main import diagonalDifference

class TestDiagonalDifference(TestCase):
    def tests_if_there_is_the_sum_of_the_main_diagonal(self):
        if diagonalDifference(self):
            return

    '''def tests_if_diagonal_sum_is_reading_the_matrix(self):
        result = diagonalDifference([[1, 1, 1], [2, 2, 2], [3,3, 3]])
        assert result.diagonal_sum() == [[1, 1, 1], [2, 2, 2], [3, 3, 3]]'''

    def test_the_result_of_main_diagonal_sum(self):
        result = diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert result.diagonal_sum() == 15

    def test_reverse_line(self):
        result = diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert result.reverse_lines() == [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

    def test_absolute_diference_value(self):
        result = diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert result.absolute_diference_value() == 0