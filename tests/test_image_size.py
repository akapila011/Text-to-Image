#!/usr/bin/env python3

import unittest

from TextToImage.utilities import get_image_size


class GetImageSizeTestCase(unittest.TestCase):

    def test_odd_number_of_characters_even_no_of_factors(self):
        text_length = 97  # becomes 98, factors = [1, 2, 7, 14, 49, 98]
        self.assertTupleEqual((14, 7), get_image_size(text_length))

    def test_even_number_of_characters_even_no_of_factors(self):
        text_length = 50  # becomes 52, factors = [1, 2, 4, 13, 26, 52]
        self.assertTupleEqual((13, 4), get_image_size(text_length))

    def test_odd_number_of_characters_odd_no_of_factors(self):
        text_length = 99  # becomes 100, factors = [1, 2, 4, 5, 10, 20, 25, 50, 100]
        self.assertTupleEqual((10, 10), get_image_size(text_length))

    def test_large_number_of_characters(self):
        text_length = 9999999  # becomes 10000000
        self.assertTupleEqual((3200, 3125), get_image_size(text_length))

    def test_number_of_characters_is_a_prime_number(self):
        text_length = 1231  # becomes 1232
        self.assertTupleEqual((44, 28), get_image_size(text_length))


if __name__ == "__main__":
    unittest.main()