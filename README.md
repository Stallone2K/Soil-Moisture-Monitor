# IOT : Soil Moisture Monitor Raspberry Pi 3

![Project Logo](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e619a261-38db-4f2b-b620-6df273a4e23f/CULOGO.png)

---

## AWS Documentation: (The Idea)

[Monitoring soil moisture with AWS IoT and Raspberry Pi](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-tutorial.html)

---

### Alterations:

- Email == WhatsApp (Twilio API)
- No Data Stored
- Threshold Moisture Value Set To = 300

### Problem Statement:

In India, agriculture is the main source of livelihood for many people and has a major impact on the economy. Water consumption is increasing daily, leading to potential water scarcity issues. This project aims to help both farmers and homeowners maintain optimal soil moisture levels efficiently.

## Pi Configuration:

### Circuit Diagram:

![Circuit Diagram](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e3c8a25a-a246-4630-966a-4fe625be1965/Pi.png)

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

![GPIO Pins](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c86234df-0d8b-4e72-ac30-f9b26c715718/Raspberry_pi_3_GPIO_pins_v2.png)

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

![Sensor Image](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/637ad011-c927-4959-9eff-787245dd719d/WhatsApp_Image_2021-05-04_at_11.58.18_AM.jpeg)
