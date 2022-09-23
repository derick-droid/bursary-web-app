from django import forms

class PersonalForm():
    name = forms.CharField()
    gender = forms.ChoiceField(choices=[("male", "Male")("female", "Female") ("other", "Other")], widget=forms.RadioSelect)
    DATE_OF_BIRTH = forms.TimeField(required = True, label="DATE OF BIRTH")
    ID_NO_passport = forms.IntegerField(required=True, label="ID.NO/PASSPORT")
    