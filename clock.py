from time import *
from os import *
n=int(input("enter 1 to use timer \nenter 2 to use clock\nenter 3 to use stopwatch\n :"))
#timer function
def timer(hours=0,minutes=0,seconds=0):
	usertime=hours*3600+minutes*60+seconds
	currtime=time()
	endtime=currtime+usertime
	
	while time()<endtime:
		remainsec=int(endtime-time())
		remainhour=int(remainsec/3600)
		remainmin= (remainsec% 3600)//60
		remainsec%= 60 
		print(f"  {remainhour}:{remainmin}:{remainsec}")
	sleep(1)
#check the alarm file then enter path
#startfile("Desktop\\python\\Alarm.mp3")
#print("TIME'S UP!!!")	
#alarm function
def alarm(hours=0,minutes=0,seconds=0):
	
	
    while True:
        alarmtime=int(hours*3600+minutes*60)
        endtime=alarmtime
        currtime = time()
        if currtime >endtime:
            break
    sleep(1)
	
#stopwatch function
def stopwatch():
    starttime = time()
    while True:
        gonetime = time() - starttime
        min = int(gonetime // 60)
        sec = int(gonetime % 60)
        print(f"{min}:{sec}")
        sleep(1)	
#timer	
if n==1:
	hours=int(input("Enter hour : "))
	min=int(input("Enter minutes : "))
	sec=int(input("Enter seconds : "))
	timer(hours,min,sec)
	system(cls)
	print("TIME'S UP!!!")
	startfile("Desktop\\python\\Alarm.mp3")
	

#alarm	
elif n==2:
	hour=int(input("Enter hour : "))
	min=int(input("Enter minutes : "))
	alarm(hour,min)
	print("WAKE UP!!!")
	startfile("Desktop\\python\\Alarm.mp3")
#stopwatch
elif n==3:
	print("Enter 'control-C' to stop : ")
	stopwatch()
	startfile("Desktop\\python\\Alarm.mp3")
else:
	print("INVALID INPUT")
