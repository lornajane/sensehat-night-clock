# Run this every so on, it will check the time and update the clock display
# Works well with cron

import time
import math
from sense_hat import SenseHat
sense = SenseHat()
sense.clear(0,0,0)

on = 100 # this might be too bright
half = int(on * 0.5)
more = int(on * 0.7)
less = int(on * 0.3)

def draw_minutes(area):
    if area == 0:
        sense.set_pixel(3,0, (on, on, on))
        sense.set_pixel(4,0, (on, on, on))

    if area == 1:
        sense.set_pixel(5,1, (on, on, on))

    if area == 2:
        sense.set_pixel(6,2, (on, on, on))

    if area == 3:
        sense.set_pixel(7,3, (on, on, on))
        sense.set_pixel(7,4, (on, on, on))

    if area == 4:
        sense.set_pixel(6,5, (on, on, on))

    if area == 5:
        sense.set_pixel(5,6, (on, on, on))

    if area == 6:
        sense.set_pixel(4,7, (on, on, on))
        sense.set_pixel(3,7, (on, on, on))

    if area == 7:
        sense.set_pixel(2,6, (on, on, on))

    if area == 8:
        sense.set_pixel(1,5, (on, on, on))

    if area == 9:
        sense.set_pixel(0,4, (on, on, on))
        sense.set_pixel(0,3, (on, on, on))

    if area == 10:
        sense.set_pixel(1,2, (on, on, on))

    if area == 11:
        sense.set_pixel(2,1, (on, on, on))

print(time.strftime("%H"))
print(time.strftime("%M"))
# sense.set_pixel(3, 3, (0, 0, 255))

# hour indicated by central colour

hour = int(time.strftime("%H")) % 12

colours = {
    0: (on, 0,0), # red
    1: (on, half,0), # orange
    2: (on, on,0), # yellow
    3: (half, more,0), # spring green
    4: (0,on, 0), # green
    5: (0,on, half ), # aqua
    6: (less, half,on), # light blue
    7: (0,0, on), # dark blue
    8: (half, 0,on), # purple
    9: (on, 0,on), # magenta
    10: (on, half,more), # baby pink 
    11: (on, on ,half), # cream
}

# write the central blob
sense.set_pixel(3,3, colours[hour])
sense.set_pixel(3,4, colours[hour])
sense.set_pixel(4,3, colours[hour])
sense.set_pixel(4,4, colours[hour])

# this way is up
sense.set_pixel(0,0,(half, half, half))
sense.set_pixel(7,0,(half, half, half))

# now the minutes
mins = int(time.strftime("%M")) 

# 12 rough areas on the clock
area = math.floor(mins / 5)
print(area)
draw_minutes(area)

# # cute debugging
# x = 0
# y = 0
# 
# for i in range(0, 11):
#     print(colours[i])
#     sense.set_pixel(x,y, colours[i]);
#     x += 1
# 
#     if x > 5:
#         x = 0
#         y = 1
# 

# for j in range (0, 11):
#     draw_minutes(j)
#     time.sleep(1)

