# IOT : Soil Moisture Monitor Raspberry Pi 3

![Project Logo](https://raw.githubusercontent.com/Stallone2K/Soil-Moisture-Monitor/refs/heads/main/Pi.webp)

---

![CU Logo](https://raw.githubusercontent.com/Stallone2K/Soil-Moisture-Monitor/refs/heads/main/CULOGO.webp)

## AWS Documentation: (The Idea)

[Monitoring Soil Moisture With AWS IoT And Raspberry Pi](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-tutorial.html)

---

### Alterations:

- Email == WhatsApp (Twilio API)
- No Data Stored
- Threshold Moisture Value Set To = 300

### Problem Statement:

In India, agriculture is the main source of livelihood for many people and has a major impact on the economy. Water consumption is increasing daily, leading to potential water scarcity issues. This project aims to help both farmers and homeowners maintain optimal soil moisture levels efficiently.

## Pi Configuration:

### Circuit Diagram:

![Circuit Diagram](https://raw.githubusercontent.com/Stallone2K/Soil-Moisture-Monitor/refs/heads/main/Circuit.webp)

---

### Steps:

1. Install Raspbian Buster on Raspberry Pi 3B+
2. Set up the development environment (Vim/Nano Installation)
3. Install dependencies:
    - Python 3:
    ```bash
    sudo apt-get install python3
    ```
    - PiP3:
    ```bash
    sudo apt-get install python3-pip
    ```
    - RPi GPIO (Python Package):
    ```bash
    sudo apt-get install python3-rpi.gpio
    ```
    - Net Tools (for IP Configuration)
4. Enable SSH for remote accessibility
5. Install Twilio dependencies
6. Verify Pi PINS:
    ```bash
    pinout  # RPi Pin Identification
    ```

![GPIO Pins](https://raw.githubusercontent.com/Stallone2K/Soil-Moisture-Monitor/refs/heads/main/GPIO.webp)

---

## Code (Python):

```python
import RPi.GPIO as GPIO
from twilio.rest import Client 
import time, datetime

# GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# Twilio Authentication
account_sid = '****ACCOUNT_SID****' 
auth_token = '***ACCOUNT_TOKEN***' 
client = Client(account_sid, auth_token) 

message = client.messages.create( 
    from_='whatsapp:+14155238886',  
    body='WARNING: No Water Detected ',      
    to='whatsapp:+919075975133' 
)

def callback(channel):
    if GPIO.input(channel): 
        print(message.sid)
        print("No Water Detected\n")
        print("Message Sent Successfully\n")
    else:
        print("Water Detected\n", datetime)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) 
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
```

---

## Setting Up Twilio (WhatsApp Messaging):

1. Create a Twilio account
2. Navigate to **Programmable Messaging** → **Try It Out** → **Try WhatsApp**
3. Set up the **Sandbox** (Save Number e.g., +1 - - - - )
4. Complete message verification
5. Select Python as the preferred language
6. Customize text messages
7. Copy and paste the code

💡 **NOTE:** Run the following before executing the Python script:
```bash
pip3 install twilio
```

---

## SSH Into Raspberry Pi Remotely:

💡 **NOTE:** Raspberry Pi and Windows/Linux PC must be connected to the same network.

### On Raspberry Pi Terminal:
```bash
sudo apt-get update  # Update the firmware
sudo apt-get install net-tools
ifconfig  # Get IP Address (e.g., 192.168.0.9)
```

### From Windows/Linux Machine:
```bash
ssh pi@(ip_address)  # SSH into Raspberry Pi
scp <File Location> pi@(ip_address):<File Destination>  # Transfer Data
```

---

## Limitations (Drawbacks):

### **Resistive vs. Capacitive Soil Moisture Sensors**

The resistive-type soil moisture sensors are prone to corrosion, whereas capacitive soil moisture sensors are made of corrosion-resistant material, making them more durable.

#### **Resistive Soil Moisture Sensor:**
- Prone to corrosion over time due to soil acidity and electrolysis.
- Less durable.

#### **Capacitive Soil Moisture Sensor:**
- More expensive but lasts longer.
- Functions similarly to a resistive sensor but is made of anti-corrosion material.

💡 **Availability Issues Due to COVID-19**

![Sensor Image](https://raw.githubusercontent.com/Stallone2K/Soil-Moisture-Monitor/refs/heads/main/Screenshot.webp)
