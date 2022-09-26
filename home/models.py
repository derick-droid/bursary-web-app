from django.db import models

class Personal(models.Model):
        name = models.CharField( max_length=100)
        gender = models.CharField(max_length=100)
        DATE_OF_BIRTH = models.DateField()
        ID_NO_passport = models.IntegerField()
        school = models.CharField(max_length=100)
        admission_number = models.CharField(max_length=100)
        campus_branch = models.CharField(max_length=100)
        faculty_branch = models.CharField(max_length=100)
        course_study = models.CharField( max_length=100)
        mode_study = models.CharField(max_length=100)
        class_year = models.IntegerField()
        course_duration = models.IntegerField()
        year_completion = models.IntegerField()
        phone_number = models.IntegerField()
        
        def _str_(self):
            return self.name
            
        
class Polling(models.Model):
    ward =  models.CharField(max_length=100)
    location =  models.CharField(max_length=100)
    sub_location = models.CharField(max_length=100)
    physical_address =  models.IntegerField()
    permanent_address =  models.IntegerField()
    institution_post_address =  models.IntegerField()
    institution_tel_phone =  models.IntegerField()
    amount_applied = models.IntegerField()
    
    def __str__(self):
         return self.ward
    
class Family(models.Model):
    family_status = models.CharField(max_length=100)
    other_states = models.CharField(max_length=100)
    number_of_siblings= models.IntegerField()
    estimated_income = models.IntegerField()
    estimated_expenses = models.IntegerField()
    # father deatils
    father_full_name = models.CharField(max_length=100)
    father_address = models.IntegerField()
    f_phone_number =  models.IntegerField()
    father_employment =  models.CharField(max_length=100)
    father_income = models.CharField(max_length=100)
    # mother details
    mother_full_name = models.CharField(max_length=100)
    mother_address = models.IntegerField()
    m_phone_number =  models.IntegerField()
    mother_employment =  models.CharField(max_length=100)
    mother_income = models.CharField(max_length=100)
    # guradian details
    guardian_full_name = models.CharField(max_length=100)
    guardian_address = models.IntegerField()
    g_phone_number =  models.IntegerField()
    guardian_employment =  models.CharField(max_length=100)
    guardian_income = models.CharField(max_length=100)
    
    def __str__(self):
         return self.father_full_name
         
    def __str__(self):
         return self.mother_full_name
     
    def __str__(self):
         return self.guardian_full_name

