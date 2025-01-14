from django.shortcuts import render
from new.models import wordadd
from random import sample, randint
import requests

def translate(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "translation" in data:
            return data["translation"]
        else:
            return "Перевод не найден"
    else:
        return "Ошибка API"

def repeat(request):
    # Подготовка уникальных слов
    words = list(wordadd.objects.all())
    if len(words) < 4:
        return render(request, "repeat/repeatpage.html", {"error": "Недостаточно слов в базе данных."})
    
    selected_words = sample(words, 4)  # Уникальный выбор слов
    main_word = selected_words[randint(0,3)]  # Одно слово для перевода

    # Создание списка слов с переводами
    words_with_translations = []
    for word in selected_words:
        translation = translate(f"https://lingva.ml/api/v1/en/ru/{word.word}")
        words_with_translations.append({
            "word": word.word,
            "translation": translation,
            "is_correct": word == main_word
        })

    return render(request, "repeat/repeatpage.html", {
        "words": words_with_translations,
        "one_word": main_word,
    })
