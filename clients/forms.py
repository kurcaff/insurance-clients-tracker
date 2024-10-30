# forms.py
from django import forms
from .models import Client
from insurances.models import Insurance
from django.forms.widgets import TextInput

class DateInput(forms.DateInput):
    input_type = 'date'

    
class ClientForm(forms.ModelForm):
    insurances = forms.ModelMultipleChoiceField(
        queryset=Insurance.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'select2'}),
    )

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'birthday': DateInput,
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the appearance of other fields if needed
        self.fields['first_name'].widget.attrs.update({'class': 'custom-class'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter last name'})
        # Add more customizations as needed




