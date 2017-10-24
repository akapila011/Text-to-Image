#!/usr/bin/env python3

from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="text_to_image",
    version="0.0.1",
    description="Convert your text to a grayscale image and back.",
    long_description=long_description,

    url="https://github.com/akapila011/Text-to-Image",
    author="Abhishek Kapila",
    author_email="akapila011@gmail.com",

    packages=["text_to_image"],
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: Developers :: End Users",
                 "Topic :: Graphics :: Encoding :: Decoding :: Stenography",
                 "Programming Language :: Python :: 3"],
    keywords="Graphics Encoding Decoding Stenography",
    install_requires=["Pillow"]
)
