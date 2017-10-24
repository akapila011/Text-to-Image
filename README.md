# Text To Image

Easily convert your text to grayscale images and vice versa.

With this tool you can encode text or plain text files to a grayscale image to be easily shared. Each pixel represents a single character's decimal value. When decoding an image you can decode text straight to the console or to a plain text file.

<img src="Resources/words_alpha.png" alt="grayscale-image-for-dictionary"/>

Images use a PNG file extension. The image size will be automatically be set depending on the text length to be encoded.

Text should use a character encoding scheme using 8 bits or less until addditional functionality is added to support UTF-8 (16 bit). If a characte's decimal value is greater than the limit (see below) the it will be divided by the limit and the new value used. When the character value equals the limit value the new value will be 1.

The limit value passed using either command line argument -l(--limit) specifies the decimale value limit for pixel values starting from 1. The default is 256 allowing for numbers from 1 to 256 (i.e. 8 bit pixels).

##### Requirements

* Python 3.x
* Pillow (PIL fork)


## Install

You can install text_to_image using pip or setup.py

* Using pip
```bash
$> pip3 install text_to_image
```
*Note: Package is yet to be uploaded to PyPi.*

* Using setup.py. First navigative to the root directory where setup.py is located then run
```bash
$> python3 setup.py
```

## How to Use

Once installed you can either directly use the encode.py and decode.py file or import and use the relevant functions.

* Using the encode.py
```bash
$> python3 encode.py -t "Hello World!" image.png  # encodes given text
$> python3 encode.py -f my-text-file.txt image.png  # encodes a text file
$> python3 encode.py --help  # for more information on arguments
```

* Using decode.py
```bash
$> python3 decode.py image.png  # decodes a given image
$> python3 decode.py -f my-text-file.txt image.png  # decodes image.png to the given text file
$> python3 decode.py --help  # for more information on arguments
```

* Importing
```python
import text_to_image

encoded_image_path = text_to_image.encode("Hello World!", "image.png")
encoded_image_path = text_to_image.encode_file("input_text_file.txt", "output_image.png")

decoded_text = text_to_image.decode("encoded_image.png")
decoded_file_path = text_to_image.decode_to_file("encoded_image.png", "output_text_file.txt")

```

### Tests

To run tests, navigate to the root directory where setup.py is located and run

```bash
$> python3-m unittest discover tests -v
```

Another image example:

<img src="Resources/example.png" alt="another-example-image-with-encoded-text"/>

#### TODO:

* Add custom image sizes.
* Expand pixel value to allow for UTF-8 characters.

<a target='_blank' rel='nofollow' href='https://app.codesponsor.io/link/F7562BGJ3YiAu5CBEEerdT66/akapila011/Text-to-Image'>
  <img alt='Sponsor' width='888' height='68' src='https://app.codesponsor.io/embed/F7562BGJ3YiAu5CBEEerdT66/akapila011/Text-to-Image.svg' />
</a>