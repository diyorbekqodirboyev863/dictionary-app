from django import forms
from django.utils.safestring import mark_safe
from .models import Dictionary

class DictionaryForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ['en', 'ru', 'uz', 'category', 'en_pro', 'ru_pro', 'description', 'term', 'to_process']
        widgets = {
            'to_process': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form fields if needed
        self.fields['en'].widget.attrs.update({'placeholder': 'English'})
        self.fields['ru'].widget.attrs.update({'placeholder': 'Russian'})
        self.fields['uz'].widget.attrs.update({'placeholder': 'Uzbek'})
        self.fields['en_pro'].widget.attrs.update({'placeholder': 'English Pronunciation'})
        self.fields['ru_pro'].widget.attrs.update({'placeholder': 'Russian Pronunciation'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Type Description'})

    def as_div(self):
        output = []
        for field in self:
            output.append(f'<div class="form-group">{field.label_tag()}{field}</div>')
        return mark_safe('\n'.join(output))
