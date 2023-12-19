from prompt_generation import prompt_generation
import requests
import json

def get_model_res(prompt, text):

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key YOUR_API_KEY"
  }
  response = requests.post(url, headers=headers, json=prompt_generation(text))
  response_text = response.text
  response_dict = json.loads(response_text)

# Извлечение текста ответа модели
  model_response = response_dict["result"]["alternatives"][0]["message"]["text"]
  return model_response