#!/usr/bin/env python3

import argparse

from PIL import Image, ImageDraw, ImageFont

def color_hex_string(hex_string):
    if len(hex_string) != 6 and len(hex_string) != 8:
        raise argparse.ArgumentTypeError("Color must be an RGB or RGBA hex string, 6 or 8 characters long")

    for char in hex_string:
        if char not in "ABCDEFabcdef0123456789":
            raise argparse.ArgumentTypeError("Color must be an RGB or RGBA hex string.")

    return tuple([int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)])


parser = argparse.ArgumentParser(description="Generate an image from a character in a font.")

parser.add_argument("font_file", help="The font file to pull icon from.")

parser.add_argument("glyph", type=str,
    help="The Unicode code of the character to render. Ex: f0f3.")

parser.add_argument("--background-color", default="ffffff",
    dest="background_color", type=color_hex_string,
    help="Background color of image as RGB hex string.")

parser.add_argument("--fill-color", default="000000",
    dest="fill_color", type=color_hex_string,
    help="Color of character as RGB hex string.")

parser.add_argument("--font-size", default=None,
    dest="font_size", type=int,
    help="Size of character to draw in pixels. Defaults to half of image size.")

parser.add_argument("--output",
    dest="output",
    help="""Path to output generated image. The output image's format is determined by the
    file extension. If output is omitted, a preview will be shown. Note that the preview
    mechanism may not support an alpha channel.""")

parser.add_argument("--size", default=128,
    dest="size", type=int,
    help="Dimensions of output image in pixels. Defaults to %(default)d pixels.")

args = parser.parse_args()

# Default font size to half of image size.
if not args.font_size:
    args.font_size = round(args.size / 2)

glyph = bytes("\\u" + args.glyph, "ascii").decode("unicode-escape")

font = ImageFont.truetype(args.font_file, size=args.font_size)
img = Image.new("RGBA", (args.size, args.size), args.background_color)
draw = ImageDraw.Draw(img)

glyph_size = draw.textsize(glyph, font=font)
x = round((args.size - glyph_size[0]) / 2.0)
y = round((args.size - glyph_size[1]) / 2.0)

draw.text((x, y), glyph, fill=args.fill_color, font=font)

if args.output:
    img.save(args.output)
else:
    img.show()
