#!/usr/bin/env python3
import unittest

from text_to_image import encode


class EncodeTestCase(unittest.TestCase):

    def test_text_is_not_string(self):
        self.assertRaises(TypeError, encode, ["a", "b", "c"], "test_image.png", limit=256)
        self.assertRaises(TypeError, encode, 1001, "test_image.png", limit=256)
        self.assertRaises(TypeError, encode, ("a", "b", "c"), "test_image.png", limit=256)


if __name__ == "__main__":
    unittest.main()
