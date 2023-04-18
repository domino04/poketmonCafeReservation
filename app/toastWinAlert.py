from win10toast import ToastNotifier

def toastWinAlert(days):
    toaster = ToastNotifier()
    strDays =  " ".join(days)
    toaster.show_toast("포켓몬 예약 알림",f'포켓몬 예약 알림: [{strDays}]에 예약 가능')