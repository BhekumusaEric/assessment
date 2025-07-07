# test_solutions.py

import unittest
from solution import *

class TestPatternDrawing(unittest.TestCase):

    def test_draw_square(self):
        # Test drawing a solid square of stars
        # Example for height = 2:
        # **
        # **
        self.assertEqual(draw_square(2), "**\n**")

    def test_draw_pyramid(self):
        # Test drawing a centered pyramid pattern of stars
        # Example for height = 2:
        #  *
        # ***
        self.assertEqual(draw_pyramid(2), " *\n***")

    def test_draw_triangle(self):
        # Test drawing a left-aligned number triangle
        # Example for height = 3:
        # 1
        # 12
        # 123
        self.assertEqual(draw_triangle(3), "1\n12\n123")

    def test_draw_triangle_reversed(self):
        # Test drawing a reversed number triangle
        # Example for height = 3:
        # 321
        # 21
        # 1
        self.assertEqual(draw_triangle_reversed(3), "321\n21\n1")

    def test_draw_triangle_prime(self):
        # Test drawing triangle of prime numbers
        # Example for height = 2:
        # 2
        # 3 5
        self.assertEqual(draw_triangle_prime(2), "2\n3 5")

    def test_generate_identity_matrix(self):
        # Test generating a 2x2 identity matrix
        # [[1, 0],
        #  [0, 1]]
        self.assertEqual(generate_identity_matrix(2), [[1, 0], [0, 1]])

    def test_generate_zero_matrix(self):
        # Test generating a 2x3 zero matrix
        # [[0, 0, 0],
        #  [0, 0, 0]]
        self.assertEqual(generate_zero_matrix(2, 3), [[0, 0, 0], [0, 0, 0]])

    def test_border_matrix(self):
        # Test generating a 3x3 matrix with 1s on the border and 0 inside
        # [[1, 1, 1],
        #  [1, 0, 1],
        #  [1, 1, 1]]
        self.assertEqual(border_matrix(3), [[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    def test_checkerboard_pattern(self):
        # Test generating a 2x2 checkerboard pattern
        # [[0, 1],
        #  [1, 0]]
        self.assertEqual(checkerboard_pattern(2), [[0, 1], [1, 0]])

    def test_diagonal_sum(self):
        # Test calculating the sum of the main diagonal in a 2x2 matrix
        # Diagonal: 1 + 4 = 5
        self.assertEqual(diagonal_sum([[1, 2], [3, 4]]), 5)

    def test_number_triangle(self):
        # Test generating a left-aligned number triangle
        # Example for height = 3:
        # 1
        # 12
        # 123
        self.assertEqual(number_triangle(3), "1\n12\n123")

    def test_number_triangle_right_aligned(self):
        # Test generating a right-aligned number triangle
        # Example for height = 3:
        #   1
        #  12
        # 123
        self.assertEqual(number_triangle_right_aligned(3), "  1\n 12\n123")

    def test_hollow_square(self):
        # Test drawing a hollow square of stars
        # Example for height = 3:
        # ***
        # * *
        # ***
        self.assertEqual(hollow_square(3), "***\n* *\n***")

    def test_half_diamond(self):
        # Test drawing a half diamond of stars
        # Example for height = 2:
        # *
        # **
        # *
        self.assertEqual(half_diamond(2), "*\n**\n*")

    def test_full_diamond(self):
        # Test drawing a full diamond of stars
        # Example for height = 2:
        #  *
        # ***
        #  *
        self.assertEqual(full_diamond(2), " *\n***\n *")

    def test_alphabet_triangle(self):
        # Test drawing an alphabet triangle
        # Example for height = 3:
        # A
        # AB
        # ABC
        self.assertEqual(alphabet_triangle(3), "A\nAB\nABC")

    def test_binary_triangle(self):
        # Test drawing a binary triangle with alternating 0s and 1s
        # Example for height = 3:
        # 1
        # 01
        # 101
        self.assertEqual(binary_triangle(3), "1\n01\n101")

    def test_floyds_triangle(self):
        # Test drawing Floyd’s triangle
        # Example for height = 3:
        # 1
        # 2 3
        # 4 5 6
        self.assertEqual(floyds_triangle(3), "1\n2 3\n4 5 6")

    def test_pascals_triangle(self):
        # Test drawing Pascal's Triangle
        # Example for height = 4:
        # 1
        # 1 1
        # 1 2 1
        # 1 3 3 1
        self.assertEqual(pascals_triangle(4), "1\n1 1\n1 2 1\n1 3 3 1")

if __name__ == "__main__":
    unittest.main()
