#!/usr/bin/env python3
from os import path
import sys
import argparse
import logging

from PIL import Image


from text_to_image.utilities import check_filename
from text_to_image.utilities import convert_char_to_int
from text_to_image.utilities import get_image_size


def encode(text, image_path, limit=256):
    """
    Take a string of text and encode it into an 8-bit grayscale image.
    :param str text: Text may be ASCII or UTF-8 but limit value must be changed accordingly.
    :param str image_path: Path to image file. Should have a '.png' extension or no extension
    :param int limit: The value limit for each pixel. 256 = 8 bit meaning all character encoding schemes using 8 or
    fewer bit can be encoded. If limit is 65536 then character encoding schemes using 16 bits or less can be applied
    e.g. UTF-8. When a character is used from a character set greater than the limit, the character value will be
    divided by the limit value. e.g. limit=256 character=Ĭ (value=300), resulting value will be 44. For values equal to
    the limit, the resulting value will be 1 to avoid NULL within the encoded data. Limit is the number of possible
    values in decimal from 1 to a max value. (default=256 i.e. 8 bit pixels/ 1- 256 means 255 possible values)
    :return str:  The path to the image produced.
    """
    if type(text) is not str:
        raise TypeError("Parameter 'text' must be a string.")
    text_length = len(text)
    size = get_image_size(text_length)
    result_path = check_filename(image_path, extension=".png")

    img = Image.new("L", size)  # grayscale, blank black image
    ind = 0
    for row in range(0, size[0]):
        for col in range(0, size[1]):
            if ind < text_length:  # only change pixel value for length of text
                pixel_value = convert_char_to_int(text[ind], limit=limit)
                img.putpixel((row, col), pixel_value)
                ind += 1
            else:  # end of text, leave remaining pixel(s) black to indicate null
                break
    img.save(result_path)
    return result_path


def encode_file(file_path, image_path, limit=256):
    """
    Take a plain text file and encode it to a grayscale image.
    :param str file_path: Path a valid plain text file with text to be encoded. Must have a .txt extension.
    :param str image_path: Path to image to be created. Will be a png image.
    :param int limit: The value limit for each pixel. A value of 256 means 8 bit pixels and any character encoding
    scheme using fewer bits can be used. Characters with a value greater than limit will be divided by limit while
    characters equal to limit will become 1. See encode() for more information. (default = 256 i.e. 8 bit pixels).
    :return str: Path to image produced
    """
    if not path.isfile(file_path):
        raise FileExistsError("The file {0} does not exist. Cannot encode a non-existent text file.".format(file_path))
    if file_path[-4:].lower() != ".txt":
        raise TypeError("File {0} must be a plain text file with a '.txt' file extension".format(file_path))
    with open(file_path, "r") as f:
        text = f.read()

    return encode(text, image_path, limit=limit)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description="Encode text (provided or from a text file) to an image.")
    parser.add_argument("image_path", action="store", help="Filename/path for the output image with the encoded text.",
                        type=str)
    text_or_file_group = parser.add_mutually_exclusive_group()
    text_or_file_group.add_argument("-t", "--text", action="store", help="Text to be encoded.", type=str)
    text_or_file_group.add_argument("-f", "--file", action="store", help="Path to plain text file to be encoded.",
                                    type=str)
    parser.add_argument("-l", "--limit", action="store", help="Decimal value limit for pixel value (1 to max)",
                        type=int)
    args = parser.parse_args()
    if args.file is None and args.text is None:
        logging.error("You must either provide text to be encoded or a path to a text file with text to be encoded.")
        sys.exit(1)

    pixel_value_limit = 256
    if args.limit is not None:
        pixel_value_limit = args.limit

    output_file = ""  # path to created image file
    if args.text is not None:
        output_file = encode(args.text, args.image_path, limit=pixel_value_limit)
    if args.file is not None:
        output_file = encode_file(args.file, args.image_path, limit=pixel_value_limit)
    logging.info("Image '{0}' has been created".format(output_file))
