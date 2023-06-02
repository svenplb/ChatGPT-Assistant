"""
# import whisper # import whisper geht irgendwie nicht so
# speech to text mit whisper
def speech_to_text():
    # tiny, base, small, medium, large einstellbar
    model = whisper.load_model("base")
    options = {"language": "de"}

    res = model.transcribe(
        "", **options)

    print(res["text"])
"""
