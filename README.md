# Raspberry Pi I2C LCD Logger

This repository provides a utility for logging useful information from a Raspberry Pi onto an I2C LCD screen. The utility utilizes a Python driver for the I2C LCD, simplifying the process of interfacing with the LCD display.



## Contents
- <span style="font-weight: bold">lcd_driver.py</span>: This file contains the Python class lcd which provides methods for controlling the LCD display via I2C communication.
- <span style="font-weight: bold">log-data.py</span>: An example usage of the lcd class. This script continuously displays the Raspberry Pi's IP address and CPU temperature on the connected LCD screen.

## Schema
![Alt text of the image](https://github.com/cololaborde/raspberry-I2C-LCD/blob/main/image.png)


## Requirements

- Python 3.x
- <span style="font-weight: bold">smbus</span> Python library (usually pre-installed on Raspberry Pi OS)
- <span style="font-weight: bold">I2C_LCD_driver.py</span> (for the log_data.py example)

## Installation

- Ensure your Raspberry Pi has the I2C interface enabled.
- Clone this repository to your Raspberry Pi:

```bash
git clone git@github.com:cololaborde/raspberry-I2C-LCD.git
```

## Usage

1. Connect your I2C LCD to the Raspberry Pi following the previous schema.
3. Import the lcd class from lcd_driver.py into your Python script.
4. Initialize the lcd object.
5. Use the provided methods to control the LCD display.


## Driver example usage:

```bash
from time import sleep
from lcd_driver import lcd

mylcd = lcd()

while True:
    # Get IP address
    # (Replace this with your method of obtaining the IP address)
    ip = "192.168.1.100"

    # Get CPU temperature
    # (Replace this with your method of obtaining the CPU temperature)
    temp = "Temp: 45C"

    # Display IP address and CPU temperature on LCD
    mylcd.lcd_display_string(ip, 1)
    mylcd.lcd_display_string(temp, 2)

    sleep(5)  # Update every 5 seconds
```

## Auto-starting the Script

1. Create a new systemd service file:

```bash
sudo nano /etc/systemd/system/lcd_display.service
```

2. Add the following contents to the file:

```bash
[Unit]
Description=LCD Display Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /path/to/log_data.py

[Install]
WantedBy=multi-user.target
```

Replace /path/to/log_data.py with the actual path to your log_data.py script.

3. Save the file and exit the editor.
4. Reload systemd to read the new service file:

```bash
sudo systemctl daemon-reload
```

5. Enable the service to start on boot:

```bash
sudo systemctl enable lcd_display.service
```

## Credits

- Original code for the I2C interface and LCD control was compiled, modified, and made available by Denis Pleic under the GNU General Public License.
- Example usage script (log_data.py) utilizes the lcd class provided in this repository along with some system commands to display IP address and CPU temperature.

## License

This project is licensed under the GNU General Public License. See the LICENSE file for details.
