from spellchecker import (
    SpellChecker,
)  # Для исправления ошибочно транскрибированных слов

import re 

# Функция для обработки полученного с помощью транскрибации текста
# На вход получает транскрибированный текст (результат работы audio_to_text())
def text_preprocess(text):
    # Определение объекта из библиотеки SpellChecker, предназначенного для исправления ошибок транскрибации
    spell = SpellChecker(language="ru")
    # Исправление ошибок транскрибации
    corrected_text = spell.correction(text)

    # Извлечение текста без таймкодов
    text_only = re.sub(
        r"\[\d{2}:\d{2}\.\d+\s*-->\s*\d{2}:\d{2}\.\d+\]\s*", "", corrected_text
    )
    
    return text_only
