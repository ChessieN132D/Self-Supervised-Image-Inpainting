# Imports

import numpy as np
import random
import math
from PIL import Image, ImageDraw

np.random.seed(37)


# Create the mask.
def mask(im_height, im_width):
    mask = Image.new('L', (im_width, im_height), 0)
    draw = ImageDraw.Draw(mask)

    # Create each serpent of vertexes in the mask.
    for serpent_id in range(random.randint(1, 5)):
        vertex_num = random.randint(1, 7)
        x_start = random.randint(0, im_width)
        y_start = random.randint(0, im_height)
        vertex_position = [(x_start, y_start)]

        # Create each vertex line with a series of overlapping round ellipses.
        for i in range(vertex_num):
            start_point = (vertex_position[-1][0], vertex_position[-1][1])
            angle = random.uniform(0.0, 2.0) * math.pi
            vertex_length = random.randint(10, 50)
            end_point = ((start_point[0] + vertex_length * math.cos(angle)),
                         (start_point[1] + vertex_length * math.sin(angle)))
            vertex_position.append(end_point)
            ellipse_num = random.randint(75, 150)

            # Create ellipses with radius large enough so that they overlap.
            ellipse_radius = 6 * vertex_length / ellipse_num

            # Create the series of ellipses on the vertex line.
            for ell in range(ellipse_num):
                new_x = start_point[0] + ell * (end_point[0] - start_point[0]) / ellipse_num
                new_y = start_point[1] + ell * (end_point[1] - start_point[1]) / ellipse_num
                draw.ellipse([new_x - ellipse_radius, new_y - ellipse_radius,
                              new_x + ellipse_radius, new_y + ellipse_radius],
                             fill=255, outline=255, width=1)

    return mask


m = mask(128,128)
m.show()