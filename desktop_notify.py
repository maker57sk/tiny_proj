import time
from plyer import notification

if __name__ == "__main__" :
    while True:
        notification.notify(
            title = "Hello",
            message = "ok this working",
            timeout = 10
        )
        print('waiting 60 minutes')
        time.sleep(3600)
