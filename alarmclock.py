import time #import time library
import winsound #import winsound library
def alarm(): #function for producing beep
    duration=1000
    freq=440
    for i in range(10):
        winsound.Beep(freq,duration)
        time.sleep(0.1)
def get_alarm():
    print("Set alarm time in HH:MM format")
    alarm_time=input(">")
    while True:
        try:
            hour,minute=map(int,alarm_time.split(":"))
            if 0<= hour <24 and 0<= minute <60:
                return hour,minute
        except ValueError:
            print("InValid format of time")
            alarm_time=input(">")
def main():
    hour,minute=get_alarm()
    print(f"Alarm set for {hour:02d}:{minute:02d}")
    while True:
        now=time.localtime()
        if now.tm_hour==hour and now.tm_min==minute:
            print("Time's Up have to wakeup")
            alarm()
            break
        time.sleep(1)
if __name__=="__main__":
    main()


