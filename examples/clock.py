#!/usr/bin/env python

import pcd8544.lcd as lcd
import time

def main():
    lcd.init()
    lcd.text("Hello world!")
    lcd.locate(0, 4)
    lcd.text("Charlotte :-)")
    while True:
        lcd.locate(0, 1)
        lcd.text(time.strftime("%d %b %Y", time.localtime()))
        lcd.locate(0, 2)
        lcd.text(time.strftime("%H:%M:%S", time.localtime()))

        time.sleep(0.25)

if __name__ == "__main__":
    main()

