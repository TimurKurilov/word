from home.views import homepage
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name="homepage")
]
