from playsound import playsound
from datetime import datetime

now = datetime.now()

print(now)

alarm_time = input('Enter the time of alarm to be set: HH:MM:SS\n')
alarm_hour = alarm_time[:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print('Setting up alarm ... ')

# print('{}\n{}\n{}\n{}\n{}\n'.format(alarm_time, alarm_hour, alarm_minute, alarm_second, alarm_period))

while True:
    now = datetime.now()
    
    current_period = now.strftime('%p')
    current_hour = now.strftime('%I')
    current_minute = now.strftime('%M')
    current_second = now.strftime('%S')

    if(current_period == alarm_period):
        if(current_hour == alarm_hour):
            if(current_minute == alarm_minute):
                if(current_second == alarm_second):
                    print('Wake Up')
                    playsound('../alarm_sound/mixkit-facility-alarm-908.wav')
                    break