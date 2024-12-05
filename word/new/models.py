from django.db import models

class wordadd(models.Model):
    word = models.CharField(max_length=50, blank=False, unique=True)
    
