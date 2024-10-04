from django import forms
from . models import customer
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DataForm(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"
        widgets={
            'date_registered':DatePickerInput()
        }