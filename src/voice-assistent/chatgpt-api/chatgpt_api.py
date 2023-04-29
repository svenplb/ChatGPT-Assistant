# go to the api_key.py file to use your own key.

import openai
from api_key import API_KEY
import pyttsx3

userInput = input("user: ")
inputPrompt = userInput + ". Talk to me like im a dog in Shakespeare style."
openai.api_key = API_KEY
#text to speech engine
engine = pyttsx3.init()

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= inputPrompt,
  # "length" of output
  max_tokens=50,
  temperature=0
)
text = response.choices[0].text.strip()
print("assistent: ", text)

engine.say(text)

engine.runAndWait()
