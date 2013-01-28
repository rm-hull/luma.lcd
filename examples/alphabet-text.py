#!/usr/bin/env python

import pcd8544.lcd as lcd

def main():
    lcd.init()
    lcd.text(map(chr, range(0x20, 0x74)))

    lcd.backlight(1)

if __name__ == "__main__":
    main()

