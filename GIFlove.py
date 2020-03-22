import time
from board import SCL, SDA
import busio
from PIL import Image
import adafruit_ssd1306
import numpy as np

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

disp.fill(0)
disp.show()

imIN = Image.open("GIFlove.gif")


f = 0.4
fy = int(im.size[0] * f)
fx = int(im.size[1] * f)

y = 36
x = 21

for i in range(imIN.n_frames):
    imIN.seek(i)
    ip = np.asarray(imIN.resize((fy,fx)))[y:y+32,x:x+128]
    ipinv = np.zeros(ip.shape)
    for iy in range(ip.shape[0]):
        for ix in range(ip.shape[1]):
            if ip[iy,ix] > 30:
                ipinv[iy,ix] = 0
            else:
                ipinv[iy,ix] = 1
    
    disp.image(Image.fromarray(ipinv))
    disp.show()
