import whisper


def get_model(size="small"):
    model_name = size
    model = whisper.load_model(model_name)
    return model


def audio_to_text(path_to_audio, model):
    if not model:
        model = get_model()
        print("Модель была загружена.")
    result = model.transcribe(path_to_audio, language="ru", fp16=False, verbose=True)
    text = result['text']
    
    print("Видео транскрибировано.")
    # os.remove(path_to_audio)
    return text
