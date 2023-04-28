import whisper

# tiny, base, small, medium, large einstellbar
model = whisper.load_model("base")
options = {"language": "de"}

res = model.transcribe("./test_files/zu-nebenrisiken-und-wirkungen.mp3", **options)

print(res["text"])