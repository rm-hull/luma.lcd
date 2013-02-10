#!/usr/bin/env python

# TODO
#  1. Incorporate some kind of rolling average
#  2. Smaller fonts
#  3. X/Y scale
#

import os
import sys

if os.name != 'posix':
    sys.exit('platform not supported')

import time
import math
import psutil
from pcd8544 import lcd
from PIL import Image,ImageDraw

class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in xrange(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def __getitem__(self, i):
        return self.data[i]

    def __iter__(self):
        return iter(self.data)

class LooseLabels:
    """ Implements loose axis labelling from "Graphics Gems",
        /Nice Numbers for Graph Labels/, p. 61-63."""
    def __init__(self, (low, high), ntick):
        self.range = []
        r = self.__nice_num(high - low, False)
        d = self.__nice_num(r / (ntick - 1), True)
        graphmin = math.floor(low / d) * d
        graphmax = math.ceil(high / d) * d
        nfrac = int(max(-math.floor(math.log10(d)),0))
        i = graphmin
        n = graphmax + 0.5 * d

        while i < n:
            self.range.append(round(i, nfrac))
            i += d

    def __getitem__(self, i):
        return self.range[i]

    def __nice_num(self, x, rounding=False):
        if x == 0:
            return 1

        exp = int(math.floor(math.log10(x)))
        frac = x / 10**exp

        if rounding:
            nf = self.__scale(frac, [(1.5,1), (3,2), (7,5)], lambda x,y: x < y)
        else:
            nf = self.__scale(frac, [(1,1), (2,2), (5,5)], lambda x,y: x <= y)

        return nf * 10**exp

    def __scale(self, x, lookups, fn, default=10):
        for y in lookups:
            if fn(x, y[0]):
                return y[1]

        return default

class Scale:
    def __init__(self, (low,high), size):
        """ Creates a function which will translate any min/max tuple
            to the correct scaled value for display on the LCD panel """
        self.labels = LooseLabels((low,high), 5)
        offset = -self.labels[0]
        diff = (self.labels[-1] - self.labels[0]) / size
        self.fn = lambda y: size - int((y + offset) / diff)

    def __call__(self,i):
        return self.fn(i)

class LoadAverage:
    def name(self):
        return "Load Average"

    def format(self, data):
        return "%.2f %.2f %.2f" % data

    def data(self):
        return os.getloadavg()

class CpuTemperature:
    def name(self):
        return "CPU Temp"

    def format(self, data):
        return "%.1f'C" % data

    def data(self):
        res = os.popen("vcgencmd measure_temp").readline()
        return tuple([float(res.replace("temp=","").replace("'C\n",""))])

def min_max(buf):
    """ Gets the smallest and largest value from the tuples in the ring buffer """
    data = filter(lambda x: x <> None, buf)
    smallest = min(map(min, data))
    largest = max(map(max, data))
    return (smallest, largest)

def rolling_avg(cumulative_lookup, start, stop, step_size, window_size):
    for t in range(start + window_size, stop, step_size):
        total = cumulative_lookup[t] - cumulative_lookup[t - window_size]
        yield total / window_size

def render(buf):
    """ Returns an image rendering of the data in the buffer """
    im = Image.new('1', (84,48))
    draw = ImageDraw.Draw(im)
    scale = Scale(min_max(buf), im.size[1])

    for x,data in enumerate(buf):
        if data <> None:
            for y in data:
                draw.point((x,scale(y)), 1)

    del draw
    return im

def main():
    lcd.init()
    lcd.backlight(1)
    sample = CpuTemperature()
    #sample = LoadAverage()
    buf = RingBuffer(84)

    while True:
        current = sample.data()
        buf.append(current)
        lcd.image(render(buf))
        lcd.locate(0,0)
        lcd.text(sample.format(current))
        time.sleep(1)

if __name__ == "__main__":
    main()


