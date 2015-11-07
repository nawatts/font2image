# font2image
A command line tool for generating images from icon fonts

```
usage: font2image.py [-h] [--font-size [FONT_SIZE]] [--output OUTPUT]
                     [--size [SIZE]]
                     font_file glyph

Generate an image from a character in a font.

positional arguments:
  font_file             The font file to pull icon from.
  glyph                 The Unicode code of the character to render. Ex: f0f3.

optional arguments:
  -h, --help            show this help message and exit
  --font-size [FONT_SIZE]
                        Size of character to draw in pixels. Defaults to half
                        of image size.
  --output OUTPUT       Path to output generated image.
  --size [SIZE]         Dimensions of output image in pixels. Defaults to 128
                        pixels.
```
