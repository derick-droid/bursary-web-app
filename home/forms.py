
from django import forms
Gender= [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
   
    ]
MODE_OF_STUDY = [
    ("boarding", "Boarding"),
    ("regular", "Regular"),
    ("parallel", "Parallel"),
    ("day", "Day"),
]

class PersonalForm(forms.Form):

    name = forms.CharField(required = True,label="Full Names(as it appears id national ID)", max_length=100)
    gender = forms.CharField(required = True,label="Gender",widget=forms.RadioSelect(choices=Gender))
    DATE_OF_BIRTH = forms.DateField(required = True, label="DATE OF BIRTH")
    ID_NO_passport = forms.IntegerField(required=True, label="ID.NO/PASSPORT")
    school = forms.CharField(required = True,label="SCHOOL/UNIVERSITY/COLLEGE", max_length=100)
    admission_number = forms.CharField(required = True,label="ADMISSION/REGISTER NUMBER", max_length=100)
    campus_branch = forms.CharField(required = True,label="CAMPUS/BRANCH(for tertiary institution only)", max_length=100)
    faculty_branch = forms.CharField(required = True,label="FACULTY/DEPARTMENT(for tertiary institution and University)", max_length=100)
    course_study = forms.CharField(required = True,label="COURSE OF STUDY: (for tertiary institution and University) ", max_length=100)
    mode_study = forms.CharField(required=True,label="MODE OF STUDY", widget=forms.RadioSelect(choices=MODE_OF_STUDY))
    class_year = forms.IntegerField(required = True,label="CLASS / GRADE/ YEAR OF STUDY",)
    course_duration = forms.IntegerField(required = True,label="COURSE DURATION(year/s)",)
    year_completion = forms.IntegerField(required = True,label="EXPECTED YEAR AND MONTH OF COMPLETION(mm/yy)",)
    phone_number = forms.IntegerField(required = True,label="PHONE NUMBER:",)


class PollingForm(forms.Form):
    ward =  forms.CharField(required=True, label="WARD", max_length=100)
    location =  forms.CharField(required=True, label="LOCATION", max_length=100)
    sub_location = forms.CharField(required=True, label="SUB LOCATION", max_length=100)
    physical_address =  forms.IntegerField(required=True, label="PHYSICAL ADDRRESS")
    permanent_address =  forms.IntegerField(required=True, label="PERMANENT ADDRESS")
    institution_post_address =  forms.IntegerField(required=True, label="INSTITUTION’S POSTAL ADDRESS")
    institution_tel_phone =  forms.IntegerField(required=True, label="INSTITUTION’S TELEPHONE NUMBER")
    amount_applied = forms.IntegerField(required=True, label="AMOUNT APPLIED FOR (Kshs.)")
    
   