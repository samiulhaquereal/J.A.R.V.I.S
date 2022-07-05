import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import requests , Camera
from bs4 import BeautifulSoup
from translate import Translator
from gtts import gTTS
from playsound import playsound
import os , banglaq
from random import randint


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.setProperty('rate',170)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def ques():
    while True:
        query = takecommand().lower()
        if 'tell me about' in query:
            query = query.replace("tell me about","")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikipedia"+results)
        elif 'who made you' in query:
            speak("Great Coder , B M Samiul Haque Real was made me, by using Python")
        elif 'your name' in query:
            speak("I am jarvis .")

        elif 'check' in query:
            l = int(query.replace('check',''))
            if (l % 4) == 0:
                if (l % 100) == 0:
                    if (l % 400) == 0:
                        speak(f"{l} is a leap year")
                    else:
                        speak(f"{l} is not a leap year")
                else:
                    speak(f"{l} is a leap year")
            else:
                speak(f"{l} is not a leap year")

        elif 'leap year' in query:
            a= datetime.datetime.today()
            b= a.year
            if (b % 4) == 0:
                if (b % 100) == 0:
                    if (b % 400) == 0:
                        speak(f"{b} is a leap year")
                    else:
                        speak(f"{b} is not a leap year")
                else:
                    speak(f"{b} is a leap year")
            else:
                speak(f"{b} is not a leap year")

        elif 'how are you' in query:
            speak("I am good , and you?")
        elif 'weather in' in query:
            place = query.replace('weather in', '')
            search = f'weather in {place}'
            url = f"https://www.google.com/search?&q={search}"
            r = requests.get(url)
            s = BeautifulSoup(r.text,"html.parser")
            update = s.find("div",class_="BNeawe").text
            speak(update)
        elif 'can you change your language' in query:
            speak('Yes , i can , Would you like to change my language ')
            query = takecommand().lower()
            if 'yes' in query:
                textt = 'আপনার ভাষা পরিবর্তন করা হয়েছে'
                language = 'bn'
                output = gTTS(text=textt, lang=language, slow=False)
                output.save('chgentobn.mp3')
                playsound('chgentobn.mp3')
                os.remove('chgentobn.mp3')
                banglaq.ques()
            else:
                speak('ok , no problem , you already in English mode')
        elif 'languages' in query:
            speak('I only know two languages, it is Bengali and English')
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'date' in query:
            date = datetime.datetime.now().strftime('%d:%B %Y')
            speak('Current Date is ' + date)
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
        elif 'what is the meaning of' in query:
            i = query.replace('what is the meaning of','')
            translator = Translator(to_lang="bn")
            translation = translator.translate(i)
            print(translation)
            textt = translation
            language = 'bn'
            output = gTTS(text=textt, lang=language, slow=False)
            output.save('ENTOBN.mp3')
            playsound('ENTOBN.mp3')
            os.remove('ENTOBN.mp3')

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'search' in query:
            i = query.replace('search','')
            speak('searching'+i)
            pywhatkit.search(i)

        elif 'what' in query:
            i = query
            speak('wait a secound')
            pywhatkit.search(i)








        elif 'which' in query:
            i = query
            speak('wait a secound')
            pywhatkit.search(i)
        elif 'who' in query:
            i = query
            speak('wait a secound')
            pywhatkit.search(i)
        elif 'location' in query:
            speak('Enter your IP')
            ip = input('Enter IP : ')
            res = requests.get(f'https://ipinfo.io/{ip}')
            data = res.json()
            speak(data)
        elif 'my room' in query:
            speak('Wait a second , your room now under my control')
            Camera.camera()
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'audio' in query:
            speak("I am ready . let's start")
            audio = takecommand().lower()
            textt = audio
            language = 'en'
            output = gTTS(text=textt, lang=language, slow=False)
            output.save(f'recorded{randint(1,1000)}.mp3')
            playsound('bnactive.mp3')
            os.remove('bnactive.mp3')
        elif 'bye' in query:
            speak("Thank you sir , Have a nice day , Good bye")
            exit()

if __name__ == '__main__':
    ques()