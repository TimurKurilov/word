from django.shortcuts import render
from new.models import wordadd
from random import choice
import requests

def translate(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        if "translation" in data:
            return data["translation"]
        else:
            return "Перевод не найден"
    else:
        return "Ошибка API"

def repeat(request):
    mylist = []
    mylist_translate = []
    words = list(wordadd.objects.all())
    for i in range(4):
        q = choice(words)
        mylist.append(q)
        if i == 3:
            word = q
    for w in mylist:
        translation = translate(f"https://lingva.ml/api/v1/en/ru/{w.word}")
        mylist_translate.append({"translation": translation})
    return render(request, "repeat/repeatpage.html", {"words": mylist_translate, "one_word": word})
        