from django import forms
from django.utils.safestring import mark_safe
from .models import Dictionary

class DictionaryForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ['en', 'ru', 'uz', 'category', 'en_pro', 'ru_pro', 'description', 'term', 'to_process']
        widgets = {
            'en': forms.TextInput(attrs={'placeholder': 'English'}),
            'ru': forms.TextInput(attrs={'placeholder': 'Russian'}),
            'uz': forms.TextInput(attrs={'placeholder': 'Uzbek'}),
            'en_pro': forms.TextInput(attrs={'placeholder': 'English Pronunciation'}),
            'ru_pro': forms.TextInput(attrs={'placeholder': 'Russian Pronunciation'}),
            'description': forms.Textarea(attrs={'placeholder': 'Type Description'}),
            'category': forms.Select(),
            'term': forms.Select(),
            'to_process': forms.CheckboxInput(),
        }
    def as_div(self):
        output = []
        for field in self:
            output.append(f'<div class="form-group">{field.label_tag()}{field}</div>')
        return mark_safe('\n'.join(output))