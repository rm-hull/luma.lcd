#!/usr/bin/env python
#
# !!! Needs psutil installing:
#
#    $ sudo pip install psutil
#

import os
import sys
if os.name != 'posix':
    sys.exit('platform not supported')

from datetime import datetime
import psutil
import pcd8544.lcd as lcd

# TODO: custom font bitmaps for up/down arrows
# TODO: Load histogram

def bytes2human(n):
    """
    >>> bytes2human(10000)
    '9K'
    >>> bytes2human(100001221)
    '95M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = int(float(n) / prefix[s])
            return '%s%s' % (value, s)
    return "%sB" % n
    
def cpu_usage():
    # load average, uptime
    uptime = datetime.now() - datetime.fromtimestamp(psutil.BOOT_TIME)
    av1, av2, av3 = os.getloadavg()
    return "Load:%.1f %.1f %.1f Up: %s" \
            % (av1, av2, av3, str(uptime).split('.')[0])
    
def mem_usage():
    usage = psutil.phymem_usage()
    return "Mem: %s %.0f%%" \
            % (bytes2human(usage.used), 100 - usage.percent)  

    
def disk_usage(dir):
    usage = psutil.disk_usage(dir)
    return "SD:  %s %.0f%%" \
            % (bytes2human(usage.used), usage.percent)  

def network(iface):
    stat = psutil.network_io_counters(pernic=True)[iface]
    return "%s:Tx%s,Rx%s" % \
           (iface, bytes2human(stat.bytes_sent), bytes2human(stat.bytes_recv))
    
def stats():
    lcd.cls()
    lcd.locate(0,0)
    lcd.text(cpu_usage())
    lcd.locate(1,0)
    lcd.text(mem_usage())
    lcd.locate(2,0)
    lcd.text(disk_usage('/'))
    lcd.locate(3,0)
    lcd.text(network('wlan0'))
    lcd.locate(4,0)
        
def main():
    lcd.init()
    lcd.backlight(1)
    stats()
    
if __name__ == "__main__":
    main()
