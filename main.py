import app
import time
from datetime import datetime


print("시작")

flag = True
while flag:
    now = datetime.now()
    print("searchTime: ", now.strftime('%Y-%m-%d %H:%M:%S'))
    days = app.findAvailDay()
    if len(days) > 0:
        app.toastWinAlert(days)
        if '10' in days:
            app.sendSms(days)
        if '11' in days:
            app.sendSms(days)
        if '12' in days:
            app.sendSms(days)
    
    time.sleep(60)

print("완료")