import RPi.GPIO as GPIO
from twilio.rest import Client 
import time , datetime

# SPIO SETUP

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#TWILIO TOKEN AUTHORISATION
account_sid = 'Enter SID Token Here' 
auth_token = 'Enter AUTH Token Here' 
client = Client(account_sid, auth_token) 

message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='WARNING: No Water Detected ',      
                              to='whatsapp:+919075975133' 
                          ) 

# consoleYes = "Water Detected \n"
# consoleNo = "No Water Detected \n"

def callback(channel):

    if GPIO.input (channel): 
        #Twilio Message 
        print(message.sid)
        print("No Water Detected\n")
        print("Message Sent Successfully\n")
        

    else:
        print("Water Detected\n")

GPIO.add_event_detect (channel, GPIO.BOTH, bouncetime=300) 
GPIO.add_event_callback(channel,callback)

while True:

    time.sleep(1)




 

 

 
