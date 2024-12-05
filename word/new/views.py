from django.views.generic.edit import CreateView
from .models import wordadd
from .forms import wordaddForm

class wordaddview(CreateView):
    model = wordadd
    form_class = wordaddForm
    template_name = 'add/addpage.html'
    success_url = '/add/'
