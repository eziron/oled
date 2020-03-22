import time
from PIL import Image
import Adafruit_SSD1306
import numpy as np

disp = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_bus=1, gpio=1)

disp.fill(0)
disp.show()

imIN = Image.open("GIFlove.gif")


f = 0.4
fy = int(imIN.size[0] * f)
fx = int(imIN.size[1] * f)

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
