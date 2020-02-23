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


def image_for_glyph(
    font_file,
    glyph,
    image_size=128,
    font_size=None,
    background_color=(255, 255, 255),
    fill_color=(0, 0, 0),
):
    # Default font size to half of image size.
    if font_size is None:
        font_size = round(image_size / 2)

    glyph = bytes("\\u" + glyph, "ascii").decode("unicode-escape")

    font = ImageFont.truetype(font_file, size=font_size)
    img = Image.new("RGBA", (image_size, image_size), background_color)
    draw = ImageDraw.Draw(img)

    glyph_size = draw.textsize(glyph, font=font)
    x = round((image_size - glyph_size[0]) / 2.0)
    y = round((image_size - glyph_size[1]) / 2.0)

    draw.text((x, y), glyph, fill=fill_color, font=font)

    return img


def main():
    parser = argparse.ArgumentParser(description="Generate an image from a character in a font.")

    parser.add_argument("font_file", help="The font file to pull icon from.")

    parser.add_argument("glyph", type=str,
        help="The Unicode code of the character to render. Ex: f0f3.")

    parser.add_argument("--background-color", default="ffffff",
        dest="background_color", type=color_hex_string,
        help="Background color of image as RGB hex string. Defaults to #%(default)s.")

    parser.add_argument("--fill-color", default="000000",
        dest="fill_color", type=color_hex_string,
        help="Color of character as RGB hex string. Defaults to #%(default)s.")

    parser.add_argument("--font-size", default=None,
        dest="font_size", type=int,
        help="Size of character to draw in pixels. Defaults to half of image size.")

    parser.add_argument("--image-size", default=128,
        dest="image_size", type=int,
        help="Dimensions of output image in pixels. Defaults to %(default)d pixels.")

    parser.add_argument("--output",
        dest="output",
        help="""Path to output generated image. The output image's format is determined by the
        file extension. If output is omitted, a preview will be shown. Note that the preview
        mechanism may not support an alpha channel.""")

    args = parser.parse_args()

    img = image_for_glyph(
        args.font_file,
        args.glyph,
        image_size=args.image_size,
        font_size=args.font_size,
        background_color=args.background_color,
        fill_color=args.fill_color,
    )

    if args.output:
        img.save(args.output)
    else:
        img.show()


if __name__ == "__main__":
    main()
