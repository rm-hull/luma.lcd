#!/usr/bin/env python

import time
from pcd8544 import lcd
from PIL import Image,ImageDraw,ImageFont,ImageFile

def demo():
    drawing()
    time.sleep(5)
    bitmaps()

def bitmaps():
    im = Image.new('1',(84,48))
    for filename in ["small_font.png", "gnome.png", "gogol.png", "car.png"]:
        bitmap = Image.open("images/" + filename)
        im.paste(bitmap, (0,0) + bitmap.size)

        lcd.cls()
        lcd.image(im, reverse=True)
        time.sleep(5)
        del bitmap

    del im

def drawing():
    ## Generate an image with PIL and put on the display
    ## First time through is slow as the fonts are not cached
    ##
    # load an available True Type font
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 14)

    # New b-w image
    im = Image.new('1', (84,48))

    # New drawable on image
    draw = ImageDraw.Draw(im)

    # Full screen and half-screen ellipses
    draw.ellipse((0,0,im.size[0]-1,im.size[1]-1), outline=1)
    draw.ellipse((im.size[0]/4,im.size[1]/4,im.size[0]/4*3-1,im.size[1]/4*3-1), outline=1)
    # Some simple text for a test (first with TT font, second with default
    draw.text((10,10), "hello", font=font, fill=1)
    draw.text((10,24), "world", fill=1)
    # Check what happens when text exceeds width (clipped)
    draw.text((0,0), "ABCabcDEFdefGHIghi", fill=1)

    # Copy it to the display
    lcd.image(im)

    # clean up
    del draw
    del im

if __name__ == "__main__":
    lcd.init()
    lcd.backlight(1)
    demo()
