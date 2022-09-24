from django import forms

class PersonalForm(forms.Form):
    name = forms.CharField(required = True,label="Full Names(as it appears id national ID)", max_length=100)
    gender = forms.ChoiceField(choices="gender", label="Gender")
    gender = (
        ("male, Male"),
        ("female", "Female"),
        ("other", "Other"),)
    DATE_OF_BIRTH = forms.TimeField(required = True, label="DATE OF BIRTH")
    ID_NO_passport = forms.IntegerField(required=True, label="ID.NO/PASSPORT")
    