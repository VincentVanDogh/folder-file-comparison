import os
import unittest

from src.line_difference import LineDifference
from src.main import compare_files


class FileComparisonTest(unittest.TestCase):
    lorem_expected = rf'{os.getcwd()}/data/sample1/lorem_expected.txt'
    lorem_case_sensitive = rf'{os.getcwd()}/data/sample1/lorem_v1_case_sensitive.txt'
    lorem_trailing_whitespaces = rf'{os.getcwd()}/data/sample1/lorem_v1_trailing_whitespaces.txt'

    def test_equal_files(self):
        lorem_expected_cmp: [LineDifference] = compare_files(self.lorem_expected, self.lorem_expected)
        self.assertTrue(len(lorem_expected_cmp) == 0)

    def test_compute_diff(self):
        lorem_trailing_whitespaces: [LineDifference] = compare_files(
            self.lorem_expected,
            self.lorem_trailing_whitespaces
        )
        for line in lorem_trailing_whitespaces:
            print(line.compute_diff())


if __name__ == '__main__':
    unittest.main()
