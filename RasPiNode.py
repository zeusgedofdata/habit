import requests
from gpiozero import Button
import time
from signal import pause
from gpiozero import LED


url = 'http://192.168.86.25:5000//habit'
actions = {"deorder":{"button": Button(21), "light": LED(19)}}


bad_request = LED(20)
no_response = LED(16)
success = LED(26)


#led = LED(4)
#button = Button(26)


def increment_habit(habitName, date, action):
    print("hit")
    habit = {'habitName': habitName, 'date': date}
    try:
        response = requests.post(url, data=habit)
    except:
        print("here")
        return "404"
    if response.json()["isError"]:
        return "dup"
    else:
        actions[action]["light"].on()
        return "200"
    

while True:
    response = None
    for action in actions.keys():
        if actions[action]["button"].is_pressed:
            response = increment_habit("test", "2021-12-02", action)
    if response == "200":
        success.on()
        time.sleep(1)
        success.off()
    if response == "dup":
        bad_request.on()
        time.sleep(1)
        bad_request.off()
    if response == "404":
        no_response.on()
        time.sleep(1)
        no_response.off()
    
        
        