from django import forms
from .models import MusicianModel


class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = ["first_name", "last_name", "email", "phone_number", "instrument_type"]
        widgets = {"phone_number": forms.NumberInput(attrs={"type":'tel', "pattern":"[0-9]{11}", "placeholder":"018000000000"})}
