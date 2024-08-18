import requests
import schedule
import time

mobile_number = 0857123456789

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hey, Good Morning',
        'key': 'textbelt'
    })
    print(resp.json())

# schedule.every().day.at('06:00').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)