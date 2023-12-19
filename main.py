from download_audio_from_link import download_audio_from_link
from check_input import check_input
from audio_to_text import audio_to_text, get_model
from text_preprocess import text_preprocess
from prompt_generation import prompt_generation
from get_model_res import get_model_res
import telebot

model = get_model(size="small")


def main(user_input):
    is_link = check_input(user_input)
    if is_link:
        audio_content, file_path = download_audio_from_link(user_input)
        text = audio_to_text(file_path, model)
        tokens = text_preprocess(text)
        prompt = prompt_generation(tokens)
        res = get_model_res(prompt, text)
    return res


TOKEN = "BOT-TOKEN"
bot = telebot.TeleBot(TOKEN)


# Команда '/start'
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        """\n
Привет! Я PSVL v0.1, Моя задача показывать вам краткое текстовое содержание видео.\n
Вставьте ссылку на видео с YouTube\n
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
