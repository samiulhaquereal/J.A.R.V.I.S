import speech_recognition as sr
import pyttsx3
import pyaudio
import wish
import englishq
import banglaq
from gtts import gTTS
import os
from playsound import playsound

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
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


if __name__ == '__main__':
    wish.wishnewyear()
    wish.wishme()
    #wish.weather()
    speak('What language do you want to speak ?')
    while True:
        query = takecommand().lower()
        if 'english' in query:
            speak('English is Activate , How can i help you sir')
            englishq.ques()
        elif 'bangla' in query:
            textt = 'বাংলা ভাষা চালু হয়েছে , আমি আপনাকে কীভাবে সাহায্য করতে পারি স্যার ?'
            language = 'bn'
            output = gTTS(text=textt, lang=language, slow=False)
            # speak("উইকিপিডিয়া অনুসারে"+results)
            output.save('bnactive.mp3')
            playsound('bnactive.mp3')
            os.remove('bnactive.mp3')
            banglaq.ques()
