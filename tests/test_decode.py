#!/usr/bin/env python3
import unittest
from unittest.mock import  mock_open

from TextToImage import decode


class DecodeTestCase(unittest.TestCase):

    def test_invalid_image_path_to_decode(self):
        self.assertRaises(FileExistsError, decode, "nonexistent_image.png")


if __name__ == "__main__":
    unittest.main()
