import whisper


def get_model(size="small"):
    model_name = size
    model = whisper.load_model(model_name)
    return model


def audio_to_text(path_to_audio, model):
    if not model:
        model = get_model()
        print("Модель была загружена.")
    text = model.transcribe(path_to_audio, fp16=False)
    text = [i for i in text]
    text = " ".join(text)
    print("Видео транскрибировано.")
    # os.remove(path_to_audio)
    return text
