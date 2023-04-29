import os
import playsound
import speech_recognition as sr
from gtts import gTTS

# Funktion, die den Text aussprechen kann

def speak(text):
    tts = gTTS(text=text, lang="en")
    # filname localisieren => ein fehler
    filename = "./files/voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def speak_text(text):
    with open("./files/output.txt", 'r') as f:
        text = f.read()
    tts = gTTS(text)
    tts.save('./files/output.mp3')
    os.system('mpg321 output.mp3')

# nimmt das audio vom laptop mic
def get_audio():
    r = sr.Recognizer()
    # mic anzapfen und hören
    with sr.Microphone() as source:
        auido = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(auido)
            print(said)
        except Exception as e:
            print("Exeption "+str(e))
    return said


text = get_audio()

# Open file in schreib modus
# filename localisieren => ein fehler
with open("./files/output.txt", "w") as f:
    # Reinschreiben was man gesagt hat
    f.write(text)

# wieder den text ausgeben
speak_text(text)
