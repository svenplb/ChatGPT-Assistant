import openai
from api_key import API_KEY
import pyttsx3
import speech_recognition as sr

openai.api_key = API_KEY
engine = pyttsx3.init()


def listen():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Sage etwas...")
    audio = r.listen(source)
  try:
    text = r.recognize_google(audio, language='de-DE')
    print("User: ", text)
    return text
  except sr.UnknownValueError:
    engine.say("Sorry, ich habe dich nicht verstanden. Bitte wiederhole.")
  except sr.RequestError as e:
    engine.say("Es gab einen Fehler. Bitte überprüfe deine Internetverbindung.")


while True:
    userInput = listen()
    if userInput == "exit":
      print("left the conversation")
      break

    inputPrompt = userInput + ""
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=inputPrompt,
        max_tokens=50,
        temperature=0
    )
    text = response.choices[0].text.strip()
    print("assistant: ", text)
    engine.say(text)
    engine.runAndWait()


