from socket import fromshare
from django import forms

class PersonalForm():
    name = forms.CharField()
    Gender = forms.ChoiceField.choices[("male", "male")("female", "female") ("other", "other")]
    DATE_OF_BIRTH = forms.TimeField(required = True)
    ID_NO_passport = forms.IntegerField(required=True)
    