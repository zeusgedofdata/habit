import requests
url = 'http://192.168.86.25:5000//habit'

def increment_habit(habitName, date):
    habit = {'habitName': habitName, 'date': date}
    response = requests.post(url, data=habit)
    print(response)
    print(response.text)
    
    
increment_habit("test", "2021-10-01")
