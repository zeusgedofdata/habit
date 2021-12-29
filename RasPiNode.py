import requests
from gpiozero import Button
import time
from signal import pause
from gpiozero import LED


url = 'http://192.168.86.25:5000//habit'
#brush = Button(1)
deorder = Button(26)
#shave = Button(3)
#shower = Button(4)

bad_request = LED(5)
#no_response = LED(6)
#success = LED(7)

#brush_led = LED(8)
#deorder_led = LED(9)
#shave_led = LED(10)
#show_led = LED(11)


#led = LED(4)
#button = Button(26)

def increment_habit(habitName, date):
    print("hit")
    habit = {'habitName': habitName, 'date': date}
    try:
        response = requests.post(url, data=habit)
    except:
        return "404"
    if response.json()["isError"]:
        return "dup"
    else:
        return None
    

while True:
    error = None
    if deorder.is_pressed:
        print("test")
        error = increment_habit("test", "2021-10-01")
    if error == "dup":
        led.on()
        print("error")
        time.sleep(1)
        led.off()
    if error == "404":
        led.on()
        print("error")
        time.sleep(1)
        led.off()
    time.sleep(1)
    
        
        