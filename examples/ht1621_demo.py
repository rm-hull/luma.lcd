import time

from luma.core.virtual import sevensegment
from luma.lcd.device import ht1621

device = ht1621()
seg = sevensegment(device)

seg.text = 'HELLO'

time.sleep(10)
