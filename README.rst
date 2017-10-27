Text To Image
=============

Easily convert your text to grayscale images and vice versa.

With this tool you can encode text or plain text files to a grayscale
image to be easily shared. Each pixel represents a single character’s
decimal value. When decoding an image you can decode text straight to
the console or to a plain text file.

Images use a PNG file extension. The image size will be automatically be
set depending on the text length to be encoded.

Text should use a character encoding scheme using 8 bits or less until
additional functionality is added to support UTF-8 (16 bit). If a
character’s decimal value is greater than the limit (see below) the it
will be divided by the limit and the new value used. When the character
value equals the limit value the new value will be 1.

The limit value passed using either command line argument -l(–limit)
specifies the decimal value limit for pixel values starting from 1. The
default is 256 allowing for numbers from 0 to 255 (i.e. 8 bit pixels).
If the limit value is greater than 8 bits then the value will still be
wrapped around since the output image is grayscale.

Requirements
''''''''''''

-  Python 3.x
-  Pillow (PIL fork)

Install
-------

You can install text\_to\_image using pip or setup.py

-  Using pip

   .. code:: bash

       $> pip3 install text_to_image

-  Using setup.py. First navigative to the root directory where setup.py
   is located then run

   .. code:: bash

       $> python3 setup.py install

How to Use
----------

Once installed you can either directly use the encode.py and decode.py
file or import and use the relevant functions.

-  Using the encode.py

   .. code:: bash

       $> python3 encode.py -t "Hello World!" image.png  # encodes given text
       $> python3 encode.py -f my-text-file.txt image.png  # encodes a text file
       $> python3 encode.py --help  # for more information on arguments

-  Using decode.py

   .. code:: bash

       $> python3 decode.py image.png  # decodes a given image
       $> python3 decode.py -f my-text-file.txt image.png  # decodes image.png to the given text file
       $> python3 decode.py --help  # for more information on arguments

-  Importing

   .. code:: python

       import text_to_image

	   encoded_image_path = text_to_image.encode("Hello World!", "image.png")
	   encoded_image_path = text_to_image.encode_file("input_text_file.txt", "output_image.png")

	   decoded_text = text_to_image.decode("encoded_image.png")
	   decoded_file_path = text_to_image.decode_to_file("encoded_image.png", "output_text_file.txt")


Tests
~~~~~

To run tests, navigate to the root directory where setup.py is located
and run

.. code:: bash

    $> python3-m unittest discover tests -v

Another image example:

TODO:
^^^^^

-  Add custom image sizes.
-  Expand pixel value to allow for UTF-8 characters.