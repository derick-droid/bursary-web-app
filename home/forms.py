
from django import forms
Gender= [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
   
    ]
# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]

class PersonalForm(forms.Form):
    # gender= forms.CharField(label="Gender", widget=forms.RadioSelect(choices=Gender))

    name = forms.CharField(required = True,label="Full Names(as it appears id national ID)", max_length=100)
    gender = forms.CharField(required = True,label="Gender",widget=forms.RadioSelect(choices=Gender))
    DATE_OF_BIRTH = forms.DateField(required = True, label="DATE OF BIRTH")
    ID_NO_passport = forms.IntegerField(required=True, label="ID.NO/PASSPORT")
    # favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
   