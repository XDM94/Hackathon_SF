def prompt_generation(text):
    # Обновление поля "text" в сообщении в объекте prompt
    prompt = {
        "modelUri": "gpt://GPT-TOKEN/summarization",
        "completionOptions": {"stream": False, "temperature": 0.1, "maxTokens": "2000"},
        "messages": [
            {
                "role": "system",
                "text": "Ты должен сократить переданный тебе текст. Твоя задача донести основные смысловые тезисы.",
            },
            {"role": "user", "text": "Здесь будет обработанный текст."},
        ],
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key API-KEY",
    }

    prompt["messages"][1]["text"] = text
    return prompt
