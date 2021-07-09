import pandas as pd
from time import time, sleep
import requests
from datetime import datetime, timedelta


bot_Key = '<bot_id>''
my_id = '<group_id>'
bot_api = 'https://api.telegram.org/bot' + bot_Key + '/sendmessage?chat_id=' + my_id + '&text='

presentday = datetime.now()
presentday_formatted = presentday.strftime('%d-%m-%Y')
nextday = presentday + timedelta(1)
nextday_formatted = nextday.strftime('%d-%m-%Y')

URL_1 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=302&date='+presentday_formatted
URL_2 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=302&date='+nextday_formatted


pin = [676306, 676305, 676501, 676503]


def pincode_find(n, center):

    length = len(center)
    for i in range(length):
        if center[i]['pincode']==n:
            if center[i]['sessions'][0]['available_capacity']>0:
                message = 'Place: {}\nCapacity: {}\nDose_1: {}\nDose_2: {}\nType: {}\nDate: {}'.format(center[i]['name'], center[i]['sessions'][0]['available_capacity'], center[i]['sessions'][0]['available_capacity_dose1'], center[i]['sessions'][0]['available_capacity_dose2'], center[i]['sessions'][0]['vaccine'],  center[i]['sessions'][0]['date'])
                return message
        #print(center[i]['name'],'\nAvailable_capacity:',center[i]['sessions'][0]['available_capacity'])
        #print('Dose_1:',center[i]['sessions'][0]['available_capacity_dose1'], '\nDose_2:',center[i]['sessions'][0]['available_capacity_dose2'],'\n')
  
  


while True:
    sleep(30 - time() % 30)
    df = pd.read_json(URL_1)
    center = df['centers']
    for i in pin:
        status = pincode_find(i, center)
        if status != None:
            requests.get(bot_api+status)
            print(status)
    sleep(30 - time() % 30)
    df = pd.read_json(URL_2)
    center = df['centers']
    for i in pin:
        status = pincode_find(i, center)
        if status != None:
            requests.get(bot_api+status)
            print(status)

