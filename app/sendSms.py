import sys
import ssl
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


from .env import API_KEY, API_SECRET, TO_TLNO, FROM_TLNO

def sendSms(days):
    print("sendSms start!")
    # set api key, api secret
    api_key = API_KEY
    api_secret = API_SECRET

    strDays =  " ".join(days)
    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
    params['to'] = TO_TLNO # Recipients Number '01000000000,01000000001'
    params['from'] = FROM_TLNO # Sender number
    params['text'] = f'포켓몬 예약 알림: [{strDays}]에 예약 가능' # Message

    cool = Message(api_key, api_secret)
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])

        if "error_list" in response:
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)
    print("sendSms end")