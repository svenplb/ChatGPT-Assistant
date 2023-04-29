import os
import time

import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "C:/Users/alex0/OneDrive/Dokumente/Python_Übungen/Projekte/ChatCpt_Sprachasistent/ChatGPT-Sprachassistent/alex_text/voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    try:
        file = open(filename, 'r')
        # Do something with the file
        # Close the file
        file.close()
    except Exception as a:
        print()


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


speak("hello wie geht es dir")
get_auido()
