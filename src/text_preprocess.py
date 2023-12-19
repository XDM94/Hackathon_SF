from nltk.tokenize import (
    sent_tokenize,
    word_tokenize,
)  # Для токенизации текста для последующей передачи в модель суммаризации

from spellchecker import (
    SpellChecker,
)  # Для исправления ошибочно транскрибированных слов
import re, nltk

nltk.download("punkt")

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

    # ЧТО ПРОИСХОДИТ НИЖЕ НАДО УБРАТЬ И БЕЗ ЭТОГО ПОТЕСТИТЬ
    # Разделение на предложения
    sentences = sent_tokenize(text_only, language="russian")

    # Токенизация и удаление пунктуации
    tokens = []
    for sentence in sentences:
        words = word_tokenize(sentence.lower(), language="russian")
        words = [
            word for word in words if word.isalnum()
        ]  # Оставляем только буквенно-цифровые токены
        tokens.append(words)
    return tokens
