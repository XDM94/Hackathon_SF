import re
from pytube import YouTube

# Функция для получения аудиофайла с ютуба по ссылке с ютуба
# На вход получает уже проверенный пользовательский ввод
# На выходе после корректной работы отдаёт прочитанный аудиофайл в audio_content и путь к файлу file_path, иначе None, None
def download_audio_from_link(link):
    # Создание объекта из библиотеки YouTube для дальнейшей работы с видео по ссылке на ютубе
    video = YouTube(link)

    # Обработка возможной ошибки, если на ютуб удалили видео или нет видео по переданной ссылке
    if not video:
        print("Видео не найдено.")
        return None, None

    # Получения списка потоков аудио с видео и их сортировка по битрейту
    streams = video.streams.filter(only_audio=True).order_by("abr").desc()
    # Проверка на наличие аудиопотока видео
    if streams:
        # Выбираем аудио-поток с наивысшим битрейтом
        highest_quality_audio = streams[0]
        print(f"Загружаем аудио максимального качества: {highest_quality_audio.title}")

        # Очищаем имя файла от недопустимых символов
        clean_title = re.sub(r'[\\/*?:"<>|]', "_", video.title)

        # Формируем путь к файлу для сохранения аудио. ЗДЕСЬ НЕОБХОДИМО УКАЗАТЬ ПУТЬ К ФАЙЛУ.
        file_path = f"D:\\PATH\\TO\\FOLDER\\{clean_title}.mp3"

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
