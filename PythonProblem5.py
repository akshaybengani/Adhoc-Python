# write a code  will take  input as your name and greet you with
# good morning , good evening , goodafter noon , good night 
# as per the current time your system :
import os

time = os.popen('date +%H').readlines()
time = int(time[0])

if (time >= 6 and time <= 12):
    print("Good Morning")
elif(time > 12 and time <= 17):
    print("Good Afternoon")
elif(time > 17 and time <= 20):
    print("Good Evening")
elif (time > 20 and time <=23):
    print("Good Night")
elif (time > 0 and time < 6):
    print("Good Night")

