#!/usr/bin/env python

# Read the BMP180 sensor_table and display current values on PCD8544
#
# The table gets a row written to it every three minutes from a 
# data gathering task running on another RPi.
#
# The /shared directory is an NFS share from that other RPi.  
 
# The table has three columns
#  PRAGMA foreign_keys=OFF;
#  BEGIN TRANSACTION;
#  CREATE TABLE sensor_table (
#    date_time char(19) primary key,
#    temp real,
#    pressure real
#    );
 
# A sample row looks like
#  INSERT INTO "sensor_data" VALUES('2015-12-31 22:45:00',18.2,1006.58);
#  COMMIT;

import pcd8544.lcd as lcd
import wiringPy

import time
import datetime
import sqlite3 as sql

# Create a degree sign glyph
special_FONT = {'.' : [0x00, 0x00, 0x06, 0x09, 0x06]}

def msl(pressure,altitude=112.2):
    # Correct pressure readings @ 112.2m above mean sea level down to MSL
    # TODO Change altitude to local value
    msl = pressure/pow(1-(altitude/44330.0),5.255)
    return "%4.2f"  % (msl)

def lcd_date(date):

    lcd.locate(1,0)
    # Date in database is ISO format yyyy-mm-dd
    # Date displayed is EUR format dd/mm/yyyy
    lcd.text(date[8:10]+"/"+date[5:7]+"/"+date[0:4])

def lcd_time(ltime):
 
    lcd.locate(1,1)
    lcd.text(ltime[11:19])
 
def lcd_temp(temp):

    lcd.locate(1,2)
    lcd.text(temp)
    lcd.text('.', special_FONT)
    lcd.text('C')

def lcd_press(press):
    
    MSL = "%07.2f" % float(msl(float(press)))
    press = "%07.2f" % float(press)
    if press[0] == "0": digit_0 = " "
    else: digit_0 = press[0]
    
    lcd.locate(1,3)
    lcd.text("QFE:"+digit_0+press[1:6])

    if MSL[0] == "0": digit_0 = " "
    else: digit_0 = MSL[0]

    lcd.locate(1,4)
    lcd.text("QNH:"+digit_0+MSL[1:6])

lcd.init()
lcd.set_contrast(29)
lcd.backlight(1)

# Prime the variables in case the database is unavailable
l_date = "0000-00-00 00:00:00"
l_temp = "99.9"
l_press = "9999.99"
l_msl = "9999.99"

while True:
  endTime = datetime.datetime.now()
  sqlEnd = endTime.strftime('%Y-%m-%d %H:%M:59')
  startTime = datetime.datetime.now() - datetime.timedelta(seconds=150)
  sqlStart = startTime.strftime('%Y-%m-%d %H:%M:00')
  row = None
  sensorData = sql.connect('/shared/bmp180/sensordata.db')
  latest = sensorData.cursor()
  latest.execute("select date_time, temp, pressure from sensor_table where date_time between ? and ?",(sqlStart, sqlEnd))
  row = latest.fetchone()

  if row != None:
    l_date = str(row[0])
    l_temp = str(row[1])
    l_press = str(row[2])

  latest.close()

  lcd_date(l_date)
  lcd_time(l_date)
  lcd_temp(l_temp)
  lcd_press(l_press)
  time.sleep(30)
