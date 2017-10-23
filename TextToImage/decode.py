#!/usr/bin/env python3
from os import path
import argparse

from PIL import Image

from TextToImage.utilities import check_filename


def decode(image_path):
    """
    Decode an image by converting pixel values back to characters.
    :param str image_path: Path to a png image file.
    :return str: Decoded text.
    """
    if not path.isfile(image_path):
        raise FileExistsError("Image file {0} does not exist. Cannot decode a nonexistent image".format(image_path))
    img = Image.open(image_path)
    decoded_text = ""
    for row in range(0, img.size[0]):
        for col in range(0, img.size[1]):
            pixel_value = img.getpixel((row, col))
            if pixel_value != 0:  # ignore 0 (NULL) values
                decoded_text += chr(pixel_value)
    return decoded_text


def decode_to_file(image_path, file_path):
    """
    Take an encoded png image and produce a text file with the decoded text.
    :param str image_path: Path to a png image with encoded text to be extracted.
    :param str file_path: Path to file where decoded text will be stored. Should be a plain text file '.txt'.
    :return str: Path to output text file.
    """
    if not path.isfile(image_path):
        raise FileExistsError("Image file {0} does not exist. Cannot decode a nonexistent image".format(image_path))
    if image_path[-4:].lower() != ".png":
        raise TypeError("Image {0} must be a png image file with a '.png' file extension".format(image_path))
    file_path = check_filename(file_path)

    decoded_text = decode(image_path)
    with open(file_path, "w") as f:
        f.write(decoded_text)
    return file_path


if __name__ == "__main__":
    pass
