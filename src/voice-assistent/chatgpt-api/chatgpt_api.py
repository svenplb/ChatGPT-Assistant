# go to the api_key.py file to use your own key.

import os
import openai
from api_key import API_KEY

openai.api_key = API_KEY

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="can you explain how people are able to solve the rubiks cube?",
  # "length" of output
  max_tokens=5,
  temperature=0
)

print(response)

