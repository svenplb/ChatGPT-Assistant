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

# Fragen und Antworten
qa = {
    "wie geht es dir": "Mir geht es gut, danke der Nachfrage!",
    "wie spät ist es": datetime.datetime.now().strftime("%I:%M %p"),
    "wie ist das Wetter heute": "Ich bin nicht sicher. Bitte überprüfe das Wetter auf deinem Smartphone oder Computer.",
}

# Funktion, um Antworten auf Fragen zu liefern
def get_response(text):
    for question in qa:
        if question in text:
            speak(qa[question])
            return
    speak("Entschuldigung, ich habe keine Antwort auf diese Frage.")

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
        get_response(text.lower())
    except sr.UnknownValueError:
        speak("Sorry, ich habe dich nicht verstanden. Bitte wiederhole.")
    except sr.RequestError as e:
        speak("Es gab einen Fehler. Bitte überprüfe deine Internetverbindung.")

# Endlosschleife, um auf Spracheingabe zu warten
while True:
    listen()