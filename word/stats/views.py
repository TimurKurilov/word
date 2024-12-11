from django.shortcuts import render
from new.models import wordadd
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


def stats(request):
    mylist = []
    stats = wordadd.objects.all()
    for stat in stats:
        translation = translate(f"https://lingva.ml/api/v1/en/ru/{stat.word}")
        mylist.append({'word': stat.word, 'translation': translation})
    return render(request, "stats/statspage.html", {'stats': mylist})