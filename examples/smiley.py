#!/usr/bin/env python

import pcd8544.lcd as lcd

smiley = [ 0x3C,0x6E,0xD3,0xD3,0xDF,0xD3,0xD3,0x6E,0x3C ]

ch  = [0x00,0x7E,0x42,0x7E,0x4A,0x72,0x42,0x00]

def main():
    lcd.init()
    lcd.cls()
    lcd.data(smiley)
    lcd.locate(2,2)
    lcd.data(ch)
    lcd.locate(3,0)
    lcd.text("c.a.h.")
    lcd.backlight(1)

if __name__ == "__main__":
    main()
