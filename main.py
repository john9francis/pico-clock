from machine import Pin, I2C
import ssd1306
import time

# Setup I2C
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Create object
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear screen
oled.fill(0)

t = time.localtime()  # tuple: (year, month, day, hour, min, sec, weekday, yearday)

year = t[0]
month = t[1]
day = t[2]

hour = t[3]
minute = t[4]
second = t[5]

display_txt = f"{hour}:{minute}:{second} {month}/{day}/{year}"

# Draw to screen
oled.text(display_txt, 0, 0)

oled.show()
print("done!")