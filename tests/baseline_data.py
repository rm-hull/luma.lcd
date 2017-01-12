#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.rst for details.


def primitives(device, draw):
    padding = 2
    shape_width = 20
    top = padding
    bottom = device.height - padding - 1
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    x = padding
    draw.ellipse((x, top, x + shape_width, bottom), outline="red", fill="black")
    x += shape_width + padding
    draw.rectangle((x, top, x + shape_width, bottom), outline="blue", fill="black")
    x += shape_width + padding
    draw.polygon([(x, bottom), (x + shape_width / 2, top), (x + shape_width, bottom)], outline="green", fill="black")
    x += shape_width + padding
    draw.line((x, bottom, x + shape_width, top), fill="yellow")
    draw.line((x, top, x + shape_width, bottom), fill="yellow")
    x += shape_width + padding
    draw.text((x, top), 'Hello', fill="cyan")
    draw.text((x, top + 20), 'World!', fill="purple")


# These datasets are purely to prevent regression bugs from creeping in
demo_pcd8544 = [
    255, 1, 1, 1, 1, 1, 1, 1, 1, 129, 193, 65, 193, 129, 1, 1, 241, 241, 17,
    68, 68, 68, 68, 68, 68, 68, 68, 4, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 240, 15, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 240, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255
]
