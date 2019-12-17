import random
import sys
from PIL import Image, ImageOps

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

new_img = Image.new("RGB", (width, height), "white")
members = [0] * 9
for i in range(6, width // 6):
    for j in range(1, height - 1):
        members[0] = img.getpixel((i + 1, j - 1))
        members[1] = img.getpixel((i + 1, j))
        members[2] = img.getpixel((i + 1, j + 1))
        members[3] = img.getpixel((i, j - 1))
        members[4] = img.getpixel((i, j))
        members[5] = img.getpixel((i, j + 1))
        members[6] = img.getpixel((i - 1, j - 1))
        members[7] = img.getpixel((i - 1, j))
        members[8] = img.getpixel((i - 1, j + 1))
        new_img.putpixel((i, j), (random.choice(members)))

for i in range(width // 9, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, b, g))
for i in range(width // 8, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i,j),(r, b, b))
for i in range(width // 7, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, g, g))
for i in range(width // 6, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (b, r, g))
for i in range(width // 5, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (b, g, r))
for i in range(width // 4, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (b, r, r))
for i in range(width // 3, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (b, g, g))
for i in range(width // 2, width - 1):
    for j in range(1, height - 1):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (g, b, r))
new_img_invert = ImageOps.invert(new_img)
new_img_invert.save(output_path)

