import whisper
model = whisper.load_model("base")

result = model.transcribe("../../ElephantsDream.mp4")
print(result["text"])
