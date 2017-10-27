#!/usr/bin/env python3

"""
text_to_image allows you to encode text data in to a grayscale image and decode data in a garysacle image back to text.

You can encode a string using encode("text", "image_path.png", limit=256)
You can encode a plain text file using encode_file("path_to_text_file.txt", "image_path.png", limit=256)

You can decode an image to a string using decode("path_to_image.png")
You can decode an image to a string using decode_to_file("path_to_image.png", "output_file_path.txt")

Text files must have a '.txt' extension and images must have a '.png' file extension.

The limit parameter refers to the pixel value limit. The default is 256 allowing for values between 0 and 255.
If the value is greater than limit it will be wrapped around i.e. value = number % limit. When the value is equal to
the limit the new value will be 1.
This means that character encoding schemes that use the same amount of values or fewer can encode all their data in the
image without any loss i.e. 256 means 8 bit or less character encoding schemes work without loss e.g. ASCII.

Image sizes are automatically set using the length of text input.
The last pixel (or last 2 when text length is even) in an image will always have a value of 0.

"""

from .encode import encode   # only these 4 functions needed
from .encode import encode_file
from .decode import decode
from .decode import decode_to_file
