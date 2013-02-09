#!/usr/bin/env python

import os
import sys

if os.name != 'posix':
    sys.exit('platform not supported')

from datetime import datetime
import math
import psutil
import pcd8544.lcd as lcd

class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in xrange(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data

class LooseLabels:
    """ Implements loose axis labelling from "Graphics Gems",
        /Nice Numbers for Graph Labels/, p. 61-63."""
    def __init__(self, low, high, ntick):
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

    def __nice_num(self, x, rounding=False):
        exp = int(math.floor(math.log10(x)))
        frac = x / math.pow(10, exp)

        if rounding:
            nf = self.__scale(frac, [(1.5,1), (3,2), (7,5)], lambda x,y: x < y)
        else:
            nf = self.__scale(frac, [(1,1), (2,2), (5,5)], lambda x,y: x <= y)

        return nf * math.pow(10, exp)

    def __scale(self, x, lookups, fn, default=10):
        for y in lookups:
            if fn(x, y[0]):
                return y[1]

        return default

class LoadAverage:
    def name(self):
        return "Load Average"

    def data(self):
        return os.getloadavg()

class CpuTemperature:
    def name(self):
        return "CPU Temp 'C"

    def data(self):
        res = os.popen("vcgencmd measure_temp").readline()
        return tuple([float(res.replace("temp=","").replace("'C\n",""))])

def main():
    lcd.init()
    lcd.backlight(1)
    sample = CpuTemperature()
    #sample = LoadAverage()
    lcd.text("%.2f" % sample.data())

if __name__ == "__main__":
    main()


