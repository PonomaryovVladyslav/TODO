# from django.forms import ModelForm, Form
from django import forms
from todo.models import Notes


class CreateNotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['text', ]


class SearchBoxForm(forms.Form):
    text = forms.CharField()


ORDER = (
    ('text', 'By text'),
    ('created_at', 'By date')
)


class OrderingForm(forms.Form):
    order = forms.ChoiceField(choices=ORDER)
