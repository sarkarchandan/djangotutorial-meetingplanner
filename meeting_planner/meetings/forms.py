from datetime import date
from typing import Type, Dict

from django.forms import ModelForm, DateInput, TimeInput, TextInput
from django.core.exceptions import ValidationError
from .models import Meeting


class MeetingForm(ModelForm):

    class Meta:
        model: Type[Meeting] = Meeting
        fields: str = '__all__'
        widgets: Dict[str, TextInput] = {
            'date': DateInput(attrs={
                'type': 'date'
            }),
            'start': TimeInput(attrs={
                'type': 'time'
            }),
            'duration': TextInput(attrs={
                'type': 'numbers',
                'min': '1',
                'max': '4'}),
        }

    def clean_date(self) -> date:
        d: date = self.cleaned_data.get('date')
        if d < date.today():
            raise ValidationError('Meetings can not be scheduled with a past date')
        return d
