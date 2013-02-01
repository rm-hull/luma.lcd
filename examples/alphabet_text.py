#!/usr/bin/env python

import pcd8544.lcd as lcd

def demo():
    lcd.locate(0,0)
    lcd.text(map(chr, range(0x20, 0x74)))

if __name__ == "__main__":
    lcd.init()
    lcd.backlight(1)
    demo()

