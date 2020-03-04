from django.forms import ModelForm

from todo.models import Notes


class CreateNotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['text', ]