import openai
from api_key import GET_API_KEY

# info: der key funktioniert nicht sonst würde er funktionieren der code
# openai.api_key = GPT_API_KEY # hier ist ein fehler
# hier den key reintun / hier ist aber ein fehler mit dem key
openai.api_key = GET_API_KEY
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]


# funktione die dann an main.py die antwort zurück gibt
def output(text):
    antwort_main_funktion = text  # hier den text welcher von main.py kommt
    if antwort_main_funktion:
        antwort_main_funktion.append(
            {"role": "user", "content": antwort_main_funktion},
        )
        chatcpt_antwort = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=antwort_main_funktion
        )

    antwort = chatcpt_antwort.choices[0].message.content
    antwort_main_funktion.append({"role": "assistant", "content": antwort})
    return antwort


'''
# test ob chat cpt antworten funktionieren
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
'''
