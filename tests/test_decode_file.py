#!/usr/bin/env python3
import unittest
from unittest.mock import  mock_open

from text_to_image import decode_to_file


class DecodeToFileTestCase(unittest.TestCase):

    def test_image_does_not_exist(self):
        self.assertRaises(FileExistsError, decode_to_file, "nonexistent_image.png", "text_nonexistent_out_file.txt")

    def test_input_image_wrong_extension(self):
        pass  # TODO: mocking input image


if __name__ == "__main__":
    unittest.main()

