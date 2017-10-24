#!/usr/bin/env python3

import unittest
from unittest.mock import  mock_open

from text_to_image import encode_file


class EncodeFileTestCase(unittest.TestCase):

    def test_nonexistent_file_input(self):
        self.assertRaises(FileExistsError, encode_file, "nonexistent_file.txt", "file_output_image.png", limit=256)
        self.assertRaises(FileExistsError, encode_file, "nonexistent_file.TXT", "file_output_image.png", limit=256)

    def test_input_file_wrong_file_extension(self):
        # self.assertRaises(TypeError, encode_file, "test_file.png", "file_output_image.png", limit=256)
        # self.assertRaises(TypeError, encode_file, "test_file.pdf", "file_output_image.png", limit=256)
        pass   # TODO: needs mocking with text file


if __name__ == "__main__":
    unittest.main()
