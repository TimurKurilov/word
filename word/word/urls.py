from home.views import homepage
from new.views import wordaddview
from stats.views import stats
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name="homepage"),
    path('add/', wordaddview.as_view(), name="wordaddview"),
    path('stats/', stats, name="stats")
]
