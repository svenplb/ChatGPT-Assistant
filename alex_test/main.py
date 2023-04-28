# ziel ist es mit dem microphon daten einzulsen diese dann
# umändern to text
# den text dann in chatcpt rein und wieder zurück => in der funktion
# dann weider zurück geben mit der sprache

import pyaudio
import chardet
import whisper

# Definiere Parameter für die Audioaufnahme
chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
rate = 44100

# Erstelle ein PyAudio-Objekt
p = pyaudio.PyAudio()

# Öffne das Mikrofon und starte die Aufnahme
stream = p.open(format=sample_format,
                channels=channels,
                rate=rate,
                frames_per_buffer=chunk,
                input=True)

# Aufnahme starten
print("Die Aufnahme läuft...")

while True:
    data = stream.read(chunk)
    # Gib den Audioeingang in der Kommandozeile aus
    try:
        print(data.decode('utf-8'))
    except UnicodeDecodeError:
        print("Fehler: Daten konnten nicht als UTF-8 dekodiert werden.")

    count = 0
    count += 1
    if count == 100:
        break

# Beende die Aufnahme
stream.stop_stream()
stream.close()
p.terminate()
