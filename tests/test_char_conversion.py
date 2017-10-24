#!/usr/bin/env python3
import unittest

from text_to_image.utilities import convert_char_to_int


class ConvertCharToIntTestCase(unittest.TestCase):

    def test_letters_to_8bit_value(self):
        letters = sorted(("a", "b", "c", "i", "h", "o", "v", "x", "y", "q",
                          "A", "B", "C", "D", "I", "P", "Q", "R", "X", "Z", "T", "E"))
        for letter in letters:
            self.assertEqual(ord(letter), convert_char_to_int(letter, limit=256))

    def test_numbers_to_8bit_value(self):
        for no in range(0, 10):
            self.assertEqual(ord(str(no)), convert_char_to_int(str(no), limit=256))

    def test_last_char_value_for_7_8_16bit_numbers(self):
        self.assertEqual(1, convert_char_to_int(chr(128), limit=128))
        self.assertEqual(1, convert_char_to_int(chr(256), limit=256))
        self.assertEqual(1, convert_char_to_int(chr(65536), limit=65536))

    def test_raises_error_when_char_lenght_not_1(self):
        self.assertRaises(TypeError, convert_char_to_int, "abc")


if __name__ == "__main__":
    unittest.main()