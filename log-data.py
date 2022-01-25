from subprocess import Popen, PIPE
from shlex import split
import I2C_LCD_driver
from time import sleep

mylcd = I2C_LCD_driver.lcd()

while True:

    p1 = Popen(split("hostname -I"), stdout=PIPE)
    p2 = Popen(split("cut -d' ' -f1"), stdin=p1.stdout, stdout=PIPE)
    out, err = p2.communicate()
    ip = out.decode('utf-8')[:-1]
    
    p3 = Popen(split("vcgencmd measure_temp"), stdout=PIPE)
    out, err = p3.communicate()
    temp = out.decode('utf-8')[:-1]

    mylcd.lcd_display_string(str(ip),1)
    mylcd.lcd_display_string((temp),2)
    sleep(5)
