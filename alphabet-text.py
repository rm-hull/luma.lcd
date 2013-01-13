import pcd8544 as lcd

def main():
    lcd.init()
    lcd.text(map(chr, range(0x61, 0x7B)))
    lcd.locate(2, 0)
    lcd.text(map(chr, range(0x41, 0x5B)))
    lcd.locate(4, 0)

    lcd.backlight(1)

if __name__ == "__main__":
    main()

