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
    255, 1, 1, 1, 1, 129, 225, 49, 25, 13, 5, 5, 5, 5, 5, 13, 25, 49, 225, 129,
    1, 1, 1, 1, 253, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
    253, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 225, 29, 225, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 13, 49, 193, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 255, 255, 0, 0, 240,
    30, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 30, 240, 0, 0, 255, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0,
    0, 0, 224, 30, 1, 0, 1, 30, 224, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 12,
    48, 192, 0, 0, 0, 0, 0, 0, 0, 192, 255, 255, 0, 255, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 255, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 192, 60, 3, 0, 0, 0,
    0, 0, 3, 60, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 24, 96, 128,
    96, 24, 7, 0, 255, 255, 0, 127, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 192, 127, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 255, 0, 0, 0, 0, 192, 60, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 60,
    192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 224, 24, 6, 1, 6, 24, 224, 0, 255,
    255, 0, 0, 7, 60, 224, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 224, 60,
    7, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255,
    0, 0, 128, 120, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 120, 128, 0,
    0, 0, 0, 0, 192, 48, 12, 3, 0, 0, 0, 0, 0, 0, 0, 3, 255, 255, 128, 128,
    128, 128, 128, 131, 134, 140, 152, 144, 144, 176, 144, 144, 152, 140, 134,
    131, 128, 128, 128, 128, 128, 191, 160, 160, 160, 160, 160, 160, 160, 160,
    160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 191, 128, 184, 167,
    160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160,
    160, 160, 167, 184, 128, 176, 140, 131, 128, 128, 128, 128, 128, 128, 128,
    128, 128, 128, 128, 128, 255
]
