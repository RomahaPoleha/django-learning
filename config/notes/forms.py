from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note # из какой модели строить форму
        fields = ['title','content'] # поля которые показать