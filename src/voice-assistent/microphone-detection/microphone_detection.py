import os
import playsound
import speech_recognition as sr
import whisper
from gtts import gTTS
import chatgpt


# --------------------------------------------- funktionen ---------------------------------------------#
def speak(Input_Text):
    tts = gTTS(text=Input_Text, lang="en")
    # filname localisieren => ein fehler
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


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
        except Exception as error:
            print("Exeption " + str(error))
    return said


# whisper funktionen
def text_to_speech():
    with open("chatcpt_output.txt", 'r') as string:
        input_text = string.read()
    tts = gTTS(input_text)
    tts.save('output.mp3')
    os.system('mpg321 output.mp3')


def speech_to_text():
    # tiny, base, small, medium, large einstellbar
    model = whisper.load_model("base")
    options = {"language": "de"}

    res = model.transcribe(
        "", **options)

    print(res["text"])


# --------------------------------------------- main code ---------------------------------------------#
print("Anfang des codes")

try:
    text = get_auido()
    # Open file in schreib modus
    # überprüfen ob die eingabe stimmt
    with open("output.txt", "w") as f:
        # Reinschreiben was man gesagt hat
        f.write(text)

except Exception as e:
    print(e)

# classe chatcpt den text geben und chat cpt fragen mit dem text
try:
    # hier zur andern klasse dann den chatcpt text zurück geben
    # hier ist ein fehler und ich weiß nicht wie es geht mit den klassen
    chatcpt_text = chatgpt.output(text)

    # Open file in schreib modus
    # überprüfen ob die eingabe stimmt
    with open("chatcpt_output.txt", "w") as f:
        # Reinschreiben was man gesagt hat
        f.write(chatcpt_text)

except Exception as e:
    print(e)

# die nachricht welche man von chatcpt erhalten hat text_to_speech
text_to_speech()
print("Ende des Programmes")
