#!/usr/bin/env python3

import unittest

from text_to_image.utilities import check_filename


class CheckFilenameTestCase(unittest.TestCase):

    def test_simple_filename_with_extension(self):
        filename = "example.txt"
        self.assertEqual(filename, check_filename("example.txt", extension=".txt"))

    def test_filename_with_no_extension(self):
        filename = "example"
        self.assertEqual(filename + ".txt", check_filename("example.txt", extension=".txt"))

    def test_windows_filepath_with_extension(self):
        filepath = r"C:\Users\User\Documents\example.txt"
        self.assertEqual(filepath, check_filename(r"C:\Users\User\Documents\example.txt", extension=".txt"))

    def test_windows_filepath_without_extension(self):
        filepath = r"C:\Users\User\Documents\example"
        self.assertEqual(filepath + ".txt", check_filename(r"C:\Users\User\Documents\example", extension=".txt"))

    def test_linux_filepath_with_extension(self):
        filepath = "/home/user/example.txt"
        self.assertEqual(filepath, check_filename("/home/user/example.txt", extension=".txt"))

    def test_linux_filepath_without_extension(self):
        filepath = "/home/user/example"
        self.assertEqual("/home/user/example" + ".txt", check_filename("/home/user/example", extension=".txt"))

    def test_filepath_without_extension_trailing_slash(self):
        filepath = "C:\\Users\\User\\Documents\\example\\"
        self.assertEqual("C:\\Users\\User\\Documents\\example" + ".txt",
                          check_filename("C:\\Users\\User\\Documents\\example\\", extension=".txt"))
        filepath = "/home/user/example/"
        self.assertEqual("/home/user/example" + ".txt", check_filename("/home/user/example", extension=".txt"))

    def test_filepath_wrong_extension(self):
        filepath = "C:\\Users\\User\\Documents\\example.png"
        self.assertNotEqual(filepath, check_filename("C:\\Users\\User\\Documents\\example.png", extension=".txt"))
        filepath = "/home/user/example.png"
        self.assertNotEqual(filepath, check_filename("/home/user/example.png", extension=".txt"))

    def test_raises_error_with_invalid_extension(self):
        self.assertRaises(ValueError, check_filename, "example.png", extension="png")


if __name__ == "__main__":
    unittest.main()
