import glob
import os
import random
from PIL import Image, ImageDraw, ImageOps

# For this code to work, you must have 9 images
# with name art.*.jpg. Each image must be 400x400 pixels.

# Create collage image
outfname = "collage.jpg"
fullimg = Image.new("RGB", (420*3+20, 420*3+20))

# Read names of images already stored
images = list(glob.glob("art.*.jpg"))
random.shuffle(images)

for i, fname in enumerate(images):
    img = Image.open(fname)

    if i%2: # we invert alternative images
        img = ImageOps.invert(img)

    # We arrange 9 images in a grid of 3x3
    offset = (20+(i//3)*420, 20+(i%3)*420)

    # Paste into collage
    fullimg.paste(img, offset)

    if i == 8: # only 9 nine images
        break

# Save collage image
fullimg.save(outfname)