import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import requests , os
from bs4 import BeautifulSoup
from translate import Translator
from gtts import gTTS
from playsound import playsound
import englishq

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.setProperty('rate', 170)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("শুনছি...")
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("দয়া করে একটু অপেক্ষা করুন....")
        query = r.recognize_google(audio, language='bn')
        print(f"ব্যবহারকারী বলেছেন: {query}\n")

    except Exception as e:
        #print(e)
        print("দয়া করে আবার বলুন...")
        return "None"
    return query
def ques():
    while True:
        query = takecommand().lower()
        if 'সম্পর্কে কিছু বলুন' in query:
            query = query.replace("সম্পর্কে কিছু বলুন","")
            results = wikipedia.summary(query, sentences=2 )
            print(results)
            language = 'bn'
            output = gTTS(text=results , lang=language, slow=False)
            output.save('1.mp3')
            playsound('1.mp3')
            os.remove('1.mp3')
        elif 'তোমাকে কে তৈরি করেছে' in query:
            txtt = "মহৎ কোডার বি এম ছামিউল হক রিয়েল আমাকে তৈরি করেছে"
            language = 'bn'
            output = gTTS(text=txtt, lang=language, slow=False)
            output.save('2.mp3')
            playsound('2.mp3')
            os.remove('2.mp3')

        elif 'নাম' in query:
            nam = 'আমার নাম জার্বিজ'
            language = 'bn'
            output = gTTS(text=nam, lang=language, slow=False)
            # speak("উইকিপিডিয়া অনুসারে"+results)
            output.save('3.mp3')
            playsound('3.mp3')
            os.remove('3.mp3')

        elif 'লিপ ইয়ার কিনা' in query:
            l = int(query.replace('লিপ ইয়ার কিনা',''))
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

        elif 'লিপ ইয়ার' in query:
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

        elif 'কেমন আছো' in query:
            qus = 'পুড়াই ফুরফুরা ,আপনি কেমন আছেন বস?'
            language = 'bn'
            output = gTTS(text=qus, lang=language, slow=False)
            # speak("উইকিপিডিয়া অনুসারে"+results)
            output.save('4.mp3')
            playsound('4.mp3')
            os.remove('4.mp3')

        elif 'weather in' in query:
            place = query.replace('weather in', '')
            search = f'weather in {place}'
            url = f"https://www.google.com/search?&q={search}"
            r = requests.get(url)
            s = BeautifulSoup(r.text,"html.parser")
            update = s.find("div",class_="BNeawe").text
            speak(update)
        elif 'এর ইংরেজি কি' in query:
            i = query.replace('এর ইংরেজি কি','')
            translator = Translator(from_lang="bn",to_lang="en")
            translation = translator.translate(i)
            print(translation)
            speak(translation)
        elif 'ওপেন ইউটিউব' in query:
            webbrowser.open("youtube.com")
        elif 'আজকে কত তারিখ' in query:
            date = datetime.datetime.now().strftime('%d:%B %Y')
            sxt = f'আজকে + {date}+ তারিখ '
            language = 'bn'
            output = gTTS(text=sxt, lang=language, slow=False)
            output.save('5.mp3')
            playsound('5.mp3')
            os.remove('5.mp3')

        elif 'এখন কয়টা বাজে' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            sxt = f'বর্তমান সময় + {time}'
            language = 'bn'
            output = gTTS(text=sxt, lang=language, slow=False)
            output.save('6.mp3')
            playsound('6.mp3')
            os.remove('6.mp3')
        elif 'ওপেন গুগল' in query:
            webbrowser.open("google.com")
        elif 'প্লে' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'সার্চ' in query:
            i = query.replace('search','')
            speak('searching'+i)
            pywhatkit.search(i)
        elif 'তুমি কি ভাষা পরিবর্তন করতে পারো' in query:
            speak('হ্যা, আপনি কি ভাষা পরিবর্তন করতে চান?')
            query = takecommand().lower()
            if 'হ্যা' or 'হুম' in query:
                speak('Language has been changed. English language is actived')
                englishq.ques()
            else:
                speak('আচ্ছা , সমস্যা নেই , আপনি বাংলা মোড ব্যবহার করছেন')
        elif 'কি' in query:
            i = query
            textt = 'দয়া করে একটু অপেক্ষা করুন'
            language = 'bn'
            output = gTTS(text=textt, lang=language, slow=False)
            output.save('7.mp3')
            playsound('7.mp3')
            os.remove('7.mp3')
            pywhatkit.search(i)
        elif 'কোনটি' in query:
            i = query
            textt = 'দয়া করে একটু অপেক্ষা করুন'
            language = 'bn'
            output = gTTS(text=textt, lang=language, slow=False)
            output.save('8.mp3')
            playsound('8.mp3')
            os.remove('8.mp3')
            pywhatkit.search(i)
        elif 'কে' in query:
            i = query
            textt = 'দয়া করে একটু অপেক্ষা করুন'
            language = 'bn'
            output = gTTS(text=textt, lang=language, slow=False)
            output.save('9.mp3')
            playsound('9.mp3')
            os.remove('9.mp3')
            pywhatkit.search(i)
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'আল্লাহ হাফেজ' or 'আল্লাহাফেজ' in query:
            textt = 'ধন্যবাদ স্যার, আপনার দিনটি শুভ হোক , আল্লাহ হাফেজ'
            language = 'bn'
            output = gTTS(text=textt, lang=language, slow=False)
            output.save('10.mp3')
            playsound('10.mp3')
            os.remove('10.mp3')
            exit()


if __name__ == '__main__':
    ques()

