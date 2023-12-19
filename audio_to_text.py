import whisper
import os

# Функция для получения модели whisper, по умолчанию small
def get_model(size="small"):
    model_name = size
    model = whisper.load_model(model_name)
    return model

# Функция для преобразования аудио в текст.
# На вход получает путь к файлу аудио и модель whisper
# Возвращает список текста
def audio_to_text(path_to_audio, model):
    if not model: # Если нет загруженной модели, то
        model = get_model() # она получает её из get_model
        print("Модель была загружена.")
    result = model.transcribe(path_to_audio, language="ru", fp16=False, verbose=True) # Транскрибация текста из аудио с русским языком, запускается на процессоре
    text = result['text'] # Получение текста из словаря (вывод model.transcribe)
    
    print("Видео транскрибировано.")
    os.remove(path_to_audio) # Удаление файла после его транскрибации
    return text