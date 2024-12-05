from django.shortcuts import render
from new.models import wordadd

def stats(request):
    stats = wordadd.objects.all()
    return render(request, "stats/statspage.html", {'stats': stats})