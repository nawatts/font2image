# font2image
A command line tool for generating images from icon fonts

```
usage: font2image.py [-h] [--background-color BACKGROUND_COLOR]
                     [--fill-color FILL_COLOR] [--font-size FONT_SIZE]
                     [--output OUTPUT] [--size SIZE]
                     font_file glyph

Generate an image from a character in a font.

positional arguments:
  font_file             The font file to pull icon from.
  glyph                 The Unicode code of the character to render. Ex: f0f3.

optional arguments:
  -h, --help            show this help message and exit
  --background-color BACKGROUND_COLOR
                        Background color of image as RGB hex string.
  --fill-color FILL_COLOR
                        Color of character as RGB hex string.
  --font-size FONT_SIZE
                        Size of character to draw in pixels. Defaults to half
                        of image size.
  --output OUTPUT       Path to output generated image. The output image's
                        format is determined by the file extension. If output
                        is omitted, a preview will be shown. Note that the
                        preview mechanism may not support an alpha channel.
  --size SIZE           Dimensions of output image in pixels. Defaults to 128
                        pixels.
```
