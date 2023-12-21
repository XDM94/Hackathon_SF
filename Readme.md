# Суммаризатор содержимого видеолекций
## Персональный помощник для студентов

### Решение с точки конечного пользователя
Проект представляет собой решение в виде программы, позволяющей создавать краткие конспекты видеолекций по загруженным в нее ссылкам на YouTube. 
Решение имеет следующие возможности:
- Интеграция в Telegram в виде бота, отвечающего на запросы пользователя
- Краткое изложение загруженных в нее видеороликов

### Решение с точки зрения разработчика
С точки зрения разработчика программа имеет нижеприведенный функционал:
- Загрузка и считывание аудиодорожки видео с YouTube, сохранение ее на накопителе по указанному пути
- Суммаризация текста с использованием YandexGPT
- Генерация промптов (prompt)
- Токенизация и транскрибация текста
- Преобразование загруженного аудио в текст
- Проверка на корректность данных от пользователя

---

## Начало работы

Для развертывания решения первоначально необходимо:
 - Склонировать репозиторий (`git clone [repo]`) на локальную машину по `ssh` или `https`, убедиться, что все файлы были успешно загружены.
 - В случае необходимости использования не отдельных функций, а в виде Telegram-бота указать его токен в функции `main` (`main.py`):

<details>  
<summary> Установка токена Telegram-бота </summary>

 ``` python
 TOKEN = "BOT-TOKEN"
 bot = telebot.TeleBot(TOKEN)
 ```

 </details>


- Указать YandexGPT API-KEY в функции `get_model_res`:

<details>  
<summary> Установка YandexGPT API-KEY </summary>

 ``` python

  # Необходимые модели данные для запроса. ЗДЕСЬ УКАЗЫВАЕТСЯ ВАШ API 
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key API-KEY"
  }

 ```

 </details>
 
Далее необходимо на локальной/удаленной машине запустить программу при помощи `main.py`:

<details>  
<summary> Функия main </summary>

 ``` python

 def main(user_input):
    is_link = check_input(user_input)
    if is_link:
        audio_content, file_path = download_audio_from_link(user_input)
        text = audio_to_text(file_path, model)
        tokens = text_preprocess(text)
        prompt = prompt_generation(tokens)
        res = get_model_res(prompt, text)
    return res

```
</details>

Для нормальной работы приложения необходимо скачать и установить ffmpeg.

Готово, бот можно использовать!

Если же Вас интересуют отдельные компоненты решения, импортируйте функции из соответствующих файлов по шаблону: `from [file] import [function]`.

---

## Команда проекта

Акбулатов Нурислам Марселевич - Аналитик данных

Николаев Александр Михайлович - Инженер по машинному обучению

Очкин Павел Владимирович - Аналитик данных / Scrum-мастер

Лобачев Василий Иванович - Технический писатель / Тестировщик

Хламов Денис Михайлович - Менеджер проекта / Scrum-мастер

---

### Поддержка проекта

При желании Вы можете улучшить функциональность проекта следующим способом:
- Создайте отдельную ветку
- Внесите необходимые изменения в свой репозиторий
- Сделайте pull request ваших изменений в исходную ветвь

### Лицензия

Свободно распространяемое программное обеспечение.
