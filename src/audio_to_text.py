import whisper
import torch

# Функция для получения модели whisper, по умолчанию base
def get_model():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = whisper.load_model("base").to(device)
    return model

# Функция для преобразования аудио в текст.
# На вход получает путь к файлу аудио и модель whisper
# Возвращает список текста
def audio_to_text(path_to_audio, model):
    if not model:
        model = get_model()
        print("Модель была загружена.")
    result = model.transcribe(path_to_audio, language="ru", fp16=False, verbose=True)
    text = result['text']

    print("Видео транскрибировано.")
    # os.remove(path_to_audio)
    return text
