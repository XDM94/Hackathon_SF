# Импорт всех функций проекта и telebot для запуска телеграм бота
from download_audio_from_link import download_audio_from_link
from check_input import check_input
from audio_to_text import audio_to_text, get_model
from text_preprocess import text_preprocess
from prompt_generation import prompt_generation
from get_model_res import get_model_res
import telebot

# Получение модели whsper. ЗДЕСЬ МОЖНО НАСТРОИТЬ КОРПУС (по умолчанию small)
model = get_model(size="small")

# Основная функция, которая объединяет остальные 
# На вход получает пользовательский ввод (получает от бота)
def main(user_input):
    # Получение ответа от check_input (True или False)
    is_link = check_input(user_input)
    # Если ввод проходит проверку, то 
    if is_link:
        # Получение содержимого из аудиофайла и пути к файлу
        audio_content, file_path = download_audio_from_link(user_input)
        # Транскрибация аудио
        text = audio_to_text(file_path, model)
        # Обработка текста (исправление ошибок транскрибации)
        tokens = text_preprocess(text)
        # Получение промпт-запроса к модели
        prompt = prompt_generation(tokens)
        # Получение ответа от модели yandexGPT
        res = get_model_res(prompt, text)
    else:
        res = 'Неверный формат ввода. Пожалуйста, введите корректную ссылку на видео в YouTube.'
    return res

# Указание токена бота. ЗДЕСЬ НУЖНО УКАЗАТЬ ТОКЕН.
TOKEN = "BOT-TOKEN"
# Создание объекта из библиотеки telebot и обозначение его в переменную
bot = telebot.TeleBot(TOKEN)


# Команда '/start'
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        """\n
Привет! Я PiPa v0.2, Моя задача показывать вам краткое текстовое содержание видео.\n
Вставьте ссылку на русскоязычное видео с YouTube\n
""",
    )


# Обработка сообщения от пользователя и отправление ему результата
@bot.message_handler(func=lambda message: True)
def take_input(message):
    user_input = message.text
    bot.send_message(
        message.from_user.id, "Подождите пожалуйста, ваше видео обрабатывается..."
    )
    response = main(user_input)
    bot.reply_to(message, response)


bot.polling()
