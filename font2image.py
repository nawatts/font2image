#!/usr/bin/env python3

import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

def color_hex_string(hex_string):
    return (int(hex_string[0:2], 16), int(hex_string[2:4], 16), int(hex_string[4:6], 16))

def expand_path(path):
    return os.path.realpath(os.path.expandvars(os.path.expanduser(path)))

parser = argparse.ArgumentParser(description="Generate an image from a character in a font.")

parser.add_argument("font_file", type=expand_path,
    help="The font file to pull icon from.")

parser.add_argument("glyph", type=str,
    help="The Unicode code of the character to render. Ex: f0f3.")

parser.add_argument("--background-color", nargs="?", default="ffffff",
    dest="background_color", type=color_hex_string,
    help="Background color of image as RGB hex string.")

parser.add_argument("--fill-color", nargs="?", default="000000",
    dest="fill_color", type=color_hex_string,
    help="Color of character as RGB hex string.")

parser.add_argument("--font-size", nargs="?", default=None,
    dest="font_size", type=int,
    help="Size of character to draw in pixels. Defaults to half of image size.")

parser.add_argument("--output", nargs=1,
    dest="output", type=expand_path,
    help="Path to output generated image.")

parser.add_argument("--size", nargs="?", default=128,
    dest="size", type=int,
    help="Dimensions of output image in pixels. Defaults to %(default)d pixels.")

args = parser.parse_args()

print(args)

# Default font size to half of image size.
if not args.font_size:
    args.font_size = round(args.size / 2)

glyph = bytes("\\u" + args.glyph, "ascii").decode("unicode-escape")

font = ImageFont.truetype(os.path.realpath(args.font_file), size=args.font_size)
img = Image.new("RGBA", (args.size, args.size), args.background_color)
draw = ImageDraw.Draw(img)

glyph_size = draw.textsize(glyph, font=font)
x = round((args.size - glyph_size[0]) / 2.0)
y = round((args.size - glyph_size[1]) / 2.0)

draw.text((x, y), glyph, fill=args.fill_color, font=font)

if args.output:
    img.save(os.path.realpath(args.output[0]))
else:
    img.show()
