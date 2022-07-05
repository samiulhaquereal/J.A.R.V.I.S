import datetime
import pyttsx3 , requests
from bs4 import BeautifulSoup
from random import choice

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishnewyear():
    month = int(datetime.datetime.today().month)
    day = int(datetime.datetime.today().day)
    if month == 1 and day == 1:
        speak("Happy New Year ,Boss")
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Jarvis Activate")




def weather():

    place = 'weather in Dhaka'
    url = f"https://www.google.com/search?&q={place}"
    r = requests.get(url)
    s = BeautifulSoup(r.text, "lxml")
    update = s.find("div", class_="BNeawe").text
    speak('Your current city has the current temperature is'+update)




