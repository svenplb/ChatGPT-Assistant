import os
import playsound
import speech_recognition as sr
from gtts import gTTS


# --------------------------------------------- funktionen ---------------------------------------------#
def speak():
    # tts = gTTS(text=chatgpt_text, lang="de")
    # tts.save(filename)
    filename = "output.mp3"
    playsound.playsound(filename)


# takes the audio from the device
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            audio = r.listen(source)
            try:
                input_text = r.recognize_google(audio, language="de-DE")
                # print("Check: ", input_text)
                if "hey Alex" in input_text:
                    # print("Command recognized: hey alex")
                    output_text = input_text.split("hey Alex", 1)[1]
                    break
            except sr.RequestError as error:
                print("Error", error)
                break

    return output_text


# whisper funktionen
def text_to_speech():
    with open("chatgpt_output.txt", 'r') as string:
        input_text = string.read()
    tts = gTTS(input_text, lang="de")
    tts.save('output.mp3')
    speak()


# --------------------------------------------- main code ---------------------------------------------#

# Infinite loop to wait for voice input
# while True:
try:
    main_text = get_audio()
    kurz_geschreiben = "in einem satz"
    main_text = " ".join((main_text, kurz_geschreiben))
    # Open file in write mode
    with open("output.txt", "w") as f:
        f.write(main_text)
except Exception as e:
    print(e)

# give classe chatcpt the text and ask chat cpt for the answer
try:
    import chatgpt_alex
    chatgpt_text = chatgpt_alex.output(main_text)
    print(chatgpt_text)
    # Open file in write mode
    with open("chatgpt_output.txt", "w") as f:
        f.write(chatgpt_text)
except Exception as e:
    print(e)

# the message you received from chatgpt text_to_speech
text_to_speech()

print("Ende des Programmes")
