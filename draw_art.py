import sys
import random
from PIL import Image, ImageDraw

config = {
    'count' : 10,
    'color' : {
        'random' : True,
        'fixed' : (180, 10, 240)
    },
    'shape' : 'rectangle'
}
img = Image.new("RGB", (400, 400), '#fff')
draw = ImageDraw.Draw(img)

for _ in range(config['count']):
    # Select colour
    if config['color']['random'] or config['shape'] == 'rectangle':
        rgb = random.randint(128,255), random.randint(0,255), random.randint(80,255)
    else:
        rgb = config['color']['fixed']

    # Get random endpoints for shape
    start = random.randint(0, img.size[0]), random.randint(0, img.size[1])
    end = random.randint(0, img.size[0]), random.randint(0, img.size[1])
    
    # Draw shape
    shape = config['shape']
    if shape == 'line':
        draw.line((*start, *end), fill=rgb)    
    elif shape == 'rectangle':
        draw.rectangle((*start, *end), fill=rgb)
    elif shape == 'arc':
        draw.arc((*start, *end), 0, random.randint(-180, 180), fill=rgb)
    elif shape == 'pieslice':
        draw.pieslice((*start, *end), 0, random.randint(0, 180), fill=rgb)

# Store in file
img.save("art.{}.{}.jpg".format(shape, random.randint(1000,9999)))