import speech_recognition as sr
import datetime
import pyttsx3

# Sprachengine initialisieren
engine = pyttsx3.init()

# Text-to-Speech Funktion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Aufweck-Funktion
def set_alarm(time):
    speak("Wecker wird für {} gestellt.".format(time))
    # Hier könnte z.B. eine externe Bibliothek wie "schedule" verwendet werden, um den Wecker zu stellen.

# Spracherkennungs-Funktion
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Sage etwas...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='de-DE')
        print("Du hast gesagt: " + text)
        if "aufwecken" in text and "10 Uhr 5" in text:
            set_alarm("10:05")
        else:
            speak("Ich habe nicht verstanden. Bitte wiederhole.")
    except sr.UnknownValueError:
        speak("Sorry, ich habe dich nicht verstanden. Bitte wiederhole.")
    except sr.RequestError as e:
        speak("Es gab einen Fehler. Bitte überprüfe deine Internetverbindung.")

# Endlosschleife, um auf Spracheingabe zu warten
while True:
    listen()