import os
import time

import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_auido():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        auido = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(auido)
            print(said)
        except Exception as e:
            print("Exeption "+str(e))

    return said


try:
    speak("hello")
except Exception as e:
    print(e)

# get_auido()
