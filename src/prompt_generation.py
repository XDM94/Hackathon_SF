# Функция для генерации запроса к yandexGPT
# На вход получает транскрибированный и обработанный текст
# На выходе отдаёт готовый запрос для модели в формате json
def prompt_generation(text):
    # Обновление поля "text" в сообщении в объекте prompt
    prompt = {
        # ЗДЕСЬ НЕОБХОДИМО УКАЗАТЬ ИДЕНТИФИКАТОР КАТАЛОГА НА YANDEX CLOUD
        "modelUri": "gpt://IDENTIFICATOR/summarization",
        # Параметры для настройки модели
        "completionOptions": {"stream": False, "temperature": 0.1, "maxTokens": "2000"},
        "messages": [
            {   # Определение контекста для модели
                "role": "system",
                "text": "Ты должен сократить переданный тебе текст. Твоя задача донести основные смысловые тезисы.",
            },
            # Эта строка заменяется текстом, полученным на вход функцией
            {"role": "user", "text": "Здесь будет обработанный текст."},
        ],
    }

    # Необходимые для работы параметры в запросе
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key API-KEY",
    }

    # Замена текста в запросе пользователя
    prompt["messages"][1]["text"] = text
    return prompt
