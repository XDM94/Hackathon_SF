import re
from pytube import YouTube


def download_audio_from_link(link):
    video = YouTube(link)

    if not video:
        print("Видео не найдено.")
        return None, None

    streams = video.streams.filter(only_audio=True).order_by("abr").desc()
    # streams = video.streams.filter(only_audio=True).all()
    if streams:
        # Выбираем аудио-поток с наивысшим битрейтом
        highest_quality_audio = streams[0]
        print(f"Загружаем аудио максимального качества: {highest_quality_audio.title}")

        # Очищаем имя файла от недопустимых символов
        clean_title = re.sub(r'[\\/*?:"<>|]', "_", video.title)

        # Формируем путь к файлу для сохранения аудио
        file_path = f"PATH_TO_FOLDER\\{clean_title}.mp3"

        # Загружаем аудио в файл
        highest_quality_audio.download(filename=file_path)

        # Считываем содержимое файла в переменную
        with open(file_path, "rb") as file:
            audio_content = file.read()

        print("Аудио максимального качества успешно загружено!")
        return audio_content, file_path
    else:
        print("Аудио не найдено для данного видео.")
        return None, None
