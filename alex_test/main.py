import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

# funktino die den text aussprechen kann


def speak(text):
    tts = gTTS(text=text, lang="en")
    # filname localisieren => ein fehler
    filename = "./files/voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def speack_text(text):
    with open("./files/output.txt", 'r') as f:
        text = f.read()
    tts = gTTS(text)
    tts.save('./files/output.mp3')
    os.system('mpg321 output.mp3')


# nimmt die audio von dem laptop mic
def get_auido():
    r = sr.Recognizer()
    # microphone anzapfen und hören
    with sr.Microphone() as source:
        auido = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(auido)
            print(said)
        except Exception as e:
            print("Exeption "+str(e))
    return said


text = get_auido()

# Open file in schreib modus
# filname localisieren => ein fehler
with open("./files/output.txt", "w") as f:
    # Reinschreiben was man gesagt hat
    f.write(text)

# wieder den text ausgeben
speack_text(text)
