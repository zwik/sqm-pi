# https://pypi.org/project/python-tsl2591/
from python_tsl2591 import tsl2591
import time
import math

if __name__ == '__main__':
    tsl = tsl2591() # initialize

    while True:
        full, ir = tsl.get_full_luminosity()
        lux = tsl.calculate_lux(full, ir)
        sqm = math.log((lux / 108000), 10) / -0.4
        print ("sqm:", sqm)
        time.sleep(2)
