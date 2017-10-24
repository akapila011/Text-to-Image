#!/usr/bin/env python3
from os import path
import sys
import argparse
import logging

from PIL import Image


from text_to_image.utilities import check_filename


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
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description="Decode text from an image and output to console to a text file.")
    parser.add_argument("image_path", action="store", help="Filename/path for the input image with the encoded text.",
                        type=str)
    parser.add_argument("-f", "--file", action="store", help="Path to text file where decoded text should be stored.",
                        type=str)
    args = parser.parse_args()

    if args.file is None:
        print(decode(args.image_path))
    else:
        output_file = decode_to_file(args.image_path, args.file)
        logging.info("File '{0}' has been created with the decoded text".format(output_file))
