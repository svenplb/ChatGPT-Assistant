from gtts import gTTS
import os

with open('./test_files/input.txt', 'r') as f:
    text = f.read()

tts = gTTS(text)
tts.save('output.mp3')

os.system('mpg321 output.mp3')
