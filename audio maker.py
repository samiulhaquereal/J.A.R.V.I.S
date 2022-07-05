from gtts import gTTS
from playsound import playsound



txtt = "Hey Real  ..You Have a text message"
language = 'en'
output = gTTS(text=txtt, lang=language, slow=False)
output.save('2.mp3')