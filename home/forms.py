
from dataclasses import field
from django import forms
from .models import Personal,Polling,Family
from django.forms import ModelForm
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
FAMILY_STATUS = [
    ("both parents are dead", "Both parents are dead"),
    ("one parent is dead", "One parent is dead"),
    ("both parents are a live", "Both parents are a live"),
    ("single parent", "Single parent"),
]
TYPE_EMPLOYMENT = [
    ("permanent ", "Permanent"),
    ("casual", "Casual"),
    ("contractual", "Contractual"),
    ("retired", "Retired"),
    ("self employed", "Self employed"),
    ("none", "None"),
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
    
    class Meta:
        model = Personal
        field = "__all__"


class PollingForm(forms.Form):
    ward =  forms.CharField(required=True, label="WARD", max_length=100)
    location =  forms.CharField(required=True, label="LOCATION", max_length=100)
    sub_location = forms.CharField(required=True, label="SUB LOCATION", max_length=100)
    physical_address =  forms.IntegerField(required=True, label="PHYSICAL ADDRRESS")
    permanent_address =  forms.IntegerField(required=True, label="PERMANENT ADDRESS")
    institution_post_address =  forms.IntegerField(required=True, label="INSTITUTION’S POSTAL ADDRESS")
    institution_tel_phone =  forms.IntegerField(required=True, label="INSTITUTION’S TELEPHONE NUMBER")
    amount_applied = forms.IntegerField(required=True, label="AMOUNT APPLIED FOR (Kshs.)")
    
class FamilyForm(forms.Form):
    family_status = forms.CharField(required=True, label= "Kindly indicate your family status", widget=forms.RadioSelect(choices=FAMILY_STATUS))
    other_states = forms.CharField(required=True, label="OTHERS(states)", max_length=100)
    number_of_siblings= forms.IntegerField(required=True, label="Number of siblings ( alive)",)
    estimated_income = forms.IntegerField(required=True,label="Estimated Family income(annually Kshs.)")
    estimated_expenses = forms.IntegerField(required=True, label="Estimated Family expenses(annually Kshs.)")
    # father deatils
    father_full_name = forms.CharField(label="FATHER- Full Name", max_length=100)
    father_address = forms.IntegerField(label="FATHER- ADDRESS")
    f_phone_number =  forms.IntegerField(label="FATHER-TELEPHONE NUMBER")
    father_employment =  forms.CharField(label="FATHER- Type of employment (Tick appropriately)", widget=forms.RadioSelect(choices=TYPE_EMPLOYMENT))
    father_income = forms.CharField(label="FATHER - MAIN SOURCE OF INCOME", max_length=100)
    # mother details
    mother_full_name = forms.CharField(label="MOTHER- Full Name", max_length=100)
    mother_address = forms.IntegerField(label="MOTHER- ADDRESS")
    m_phone_number =  forms.IntegerField(label="MOTHER-TELEPHONE NUMBER")
    mother_employment =  forms.CharField(label="MOTHER- Type of employment (Tick appropriately)", widget=forms.RadioSelect(choices=TYPE_EMPLOYMENT))
    mother_income = forms.CharField(label="MOTHER- MAIN SOURCE OF INCOME",max_length=100)
    # guradian details
    guardian_full_name = forms.CharField(label="GUARDIAN- Full Name", max_length=100)
    guardian_address = forms.IntegerField(label="GUARDIAN- ADDRESS")
    g_phone_number =  forms.IntegerField(label="GUARDIAN-TELEPHONE NUMBER")
    guardian_employment =  forms.CharField(label="GUARDIAN- Type of employment (Tick appropriately)", widget=forms.RadioSelect(choices=TYPE_EMPLOYMENT))
    guardian_income = forms.CharField(label="GUARDIAN- MAIN SOURCE OF INCOME", max_length=100)