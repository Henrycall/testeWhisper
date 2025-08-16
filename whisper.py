import whisper

model = whisper.load_model("turbo")  # Ou "small", "medium", "large"
result = model.transcribe("C:/Users/Henrycall/Downloads/WhatsApp Ptt 2025-06-06 at 17.23.50.ogg", language="pt")

print(result["text"])

# Para salvar em arquivo:
with open("YOU PATH HERE", "w", encoding="utf-8") as f:
    f.write(result["text"])
