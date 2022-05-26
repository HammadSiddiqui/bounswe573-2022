from django.forms import ModelForm
from .models import Majlis


class MajlisForm(ModelForm):
    class Meta:
        model = Majlis
        fields = ["title", "subtitle", "description"]