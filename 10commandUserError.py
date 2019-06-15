import os
import pyttsx3

def speak(x):
    tts = pyttsx3.init()
    rate = tts.getProperty('rate')
    tts.setProperty('rate',rate-10)
    volume = tts.getProperty('volume')
    tts.setProperty('volume',volume-1000)
    tts.say(x)
    tts.runAndWait()
for i in range(10):    
  command = input('Enter a command: ')
  os.system('command 2> error.txt')
  if (os.system('cat error.txt')):
    speak('Command not found')