#!/usr/bin/env python

import pcd8544 as lcd
import time

def main():
    lcd.init()
    lcd.text("Hello world!")
    lcd.locate(4, 0)
    lcd.text("Charlotte :-)")
    while True:
        lcd.locate(1, 0)
        lcd.text(time.strftime("%d %b %Y", time.localtime()))
        lcd.locate(2, 0)
        lcd.text(time.strftime("%H:%M:%S", time.localtime()))

        time.sleep(0.25)
        
if __name__ == "__main__":
    main()

