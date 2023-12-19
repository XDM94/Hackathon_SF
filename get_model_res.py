from prompt_generation import prompt_generation
import requests
import json


# Функция для получения результата работы yandexGPT summorization. 
# На вход получает промпт-запрос и обработанный после транскрибации текст 
# На выходе отдаёт ответ модели. Далее он булет отправлен пользователю через телеграм-бота
def get_model_res(prompt, text):

  # Адресс, необходимый для подключения модели
  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  # Необходимые модели данные для запроса. ЗДЕСЬ УКАЗЫВАЕТСЯ ВАШ API 
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key API-KEY"
  }
  # Формирование post-запроса. Здесь же передаётся промпт-запрос, сгенерированый prompt_generation
  response = requests.post(url, headers=headers, json=prompt_generation(text))
  # Получение текст из ответа модели
  response_text = response.text
  # Преобразование для работы с json
  response_dict = json.loads(response_text)

# Извлечение текста ответа модели из json
  model_response = response_dict["result"]["alternatives"][0]["message"]["text"]
  return model_response