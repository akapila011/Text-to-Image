#!/usr/bin/env python3
from functools import reduce


def check_filename(filepath, extension=".txt"):
    """
    Take a path to a file and ensure the filename has the right extension, else add the extension.
    :param str filepath: The path to the file.
    :param str extension: Extension for the given file. If wrong extension in filepath then raise error.
    Extension must start with '.'.
    :return str: The filepath with the correct extension.
    """
    if extension[0] != ".":
        raise ValueError("Parameter 'extension'  must start with a period e.g. '.txt'.")
    file_extension = filepath[-(len(extension)):].lower()  # get last part of filename to check extension
    extension = extension.lower()
    if file_extension != extension:
        # remove any trailing slashes at end of filepath
        while filepath[-1] == "/" or filepath[-1] == "\\":
            filepath = filepath[0:-1]
        filepath += extension
    return filepath


def convert_char_to_int(char, limit=256):
    """
    Take a character and return an integer value while ensuring the values returned do not go above the limit.
    :param str char: A single character.
    :param int limit: An integer representing the largest value which will start requiring reducing char value.
    (default=256).
    :return int: A number between 1 (0=NULL) and the limit that represents the int value of the char.
    """
    value = ord(char) % limit
    value = 1 if value == 0 else value
    return value


def get_image_size(text_length):
    """
    Take the length of text to be encoded and get the width, height of the resulting image.
    Must account for a null terminator at the end of the image.
    Tries to get the best resolution so that width and height values are as close as possible.
    :param int text_length: The length of text to be encoded as an image.
    :return (int, int): width, height of the image.
    """
    true_length = text_length  # True length must be an even number and include the null terminator(s) at the end.
    if text_length % 2 == 0:  # even length
        true_length = true_length + 2  # add 2 null terminators at the end
    else:  # odd length of text
        true_length += 1

    f = _factors(true_length)
    width, height = 0, 0
    if len(f) % 2 != 0:  # odd number of factors, middle value will give both width, height
        width = height = f[len(f) // 2]
    else:  # even number of factors, get middle 2 values
        while len(f) != 2:
            f.pop(0)  # remove first and last elements
            f.pop()
        width, height = f[1], f[0]  # width should be larger than height
    return width, height


def _factors(number):
    """
    Return a list of sorted numbers that can be multiplied to get the parameter (i.e. factors of parameter number).
    :param int number: Must be a positive number.
    :return [int,int]: List of factors of parameter 'number' sorted in ascending order.
    """
    if number < 0:
        raise ValueError("Parameter 'number' must be a positive value.")
    return sorted(set(reduce(list.__add__,
                             ([i, number // i] for i in range(1, int(number ** 0.5) + 1) if number % i == 0))))


if __name__ == "__main__":
    pass
