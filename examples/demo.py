#!/usr/bin/env python

import pcd8544.lcd as lcd
import time

import pi_logo
import clock
import alphabet_text
import image
import maze

from pcd8544.font import default_FONT

if __name__ == "__main__":
    lcd.init()
    lcd.backlight(1)
    
    pi_logo.demo()
    time.sleep(3)
    
    alphabet_text.demo()
    time.sleep(3)
    
    image.demo()
    time.sleep(3)
    
    maze.demo(2)
    
    clock.demo(10)
    
    lcd.cls()
    lcd.text("For details:")
    lcd.smooth_hscroll("              https://github.com/rm-hull/pcd8544  ", \
                       2, 300, delay=0.25)
    
    pi_logo.demo()
    time.sleep(3)
    lcd.backlight(0)
