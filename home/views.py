from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import PersonalForm, PollingForm, FamilyForm
from django.contrib.auth.forms import UserCreationForm


#welcome login page
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("index")
    return render(request, "home/index.html")



# sign page
def sign(request):
    if request.method == "POST":
         username = request.POST["name"]
         email = request.POST["email"]
         password = request.POST["password"]
         confirm_password = request.POST["password2"]
         
         my_user = User.objects.create_user(username, email,password)
         my_user.save()
         
         messages.success(request, "Account created successfully ")
         return redirect("home")
     
    messages.error(request, "An error occurred while creating the account ")
        

    return render(request, "home/sign.html")


# login page
def login_auth(request):

    if request.method == "POST":
        username= request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in successfully")
            return redirect("home")
        else:
            messages.error(request, "Error in loggin in")
            return redirect( "login")
    # else:
    #     return render(request, "home/login.html")
    
    return render(request, "home/login.html")

# home page
def home(request):   
    if request.method == "POST":
        form  = PersonalForm(request.POST)
   
        if form.is_valid():
            name = form.cleaned_data["name"]
            DATE_OF_BIRTH = form.cleaned_data["DATE_OF_BIRTH"]
            ID_NO_passport = form.cleaned_data["ID_NO_passport"]
            gender = form.cleaned_data["gender"]
            school = form.cleaned_data["school"]
            admission_number = form.cleaned_data["admission_number"]
            campus_branch = form.cleaned_data["campus_branch"] 
            faculty_branch = form.cleaned_data["faculty_branch"]
            course_study = form.cleaned_data["course_study"]
            mode_study =  form.cleaned_data["mode_study"]
            class_year = form.cleaned_data["class_year"]
            course_duration =  form.cleaned_data["course_duration"]
            year_completion = form.cleaned_data["year_completion"]
            phone_number  = form.cleaned_data["phone_number"]
            form.save()
            
    else:
     form = PersonalForm()
    context = {"form":form}
    return render(request, "home/home.html", context)


# polling station  form
def polling(request):
    if request.method == "POST":
        form = PollingForm(request.POST)
        
        if form.is_valid():
            ward = form.cleaned_data["ward"]
            location = form.cleaned_data["location"]
            sub_location =  form.cleaned_data["sub_location"]
            physical_address =  form.cleaned_data["physical_address"]
            permanent_address =  form.cleaned_data["permanent_address"]
            institution_post_address =  form.cleaned_data["institution_post_address"]
            institution_tel_phone  = form.cleaned_data["institution_tel_phone"]
            amount_applied = form.cleaned_data["amount_applied"]
            form.save()
            
    else:
        form = PollingForm()
    
    context = {
        "form":form,
        }

    return render(request, "home/polling.html", context)

# family form
def family(request):
    if request.method =="POST":
        form = FamilyForm(request.POST)
        
        if form.is_valid():
            family_status = form.cleaned_data["family_status"]
            other_states =  form.cleaned_data["other_states"]
            number_of_siblings =  form.cleaned_data["number_of_siblings"]
            estimated_income =  form.cleaned_data["estimated_income"]
            estimated_expenses =  form.cleaned_data["estimated_expenses"]
            # father details
            father_full_name =  form.cleaned_data["father_full_name"]
            father_address = form.cleaned_data["father_address"]
            f_phone_number =  form.cleaned_data["f_phone_number"]
            father_employment = form.cleaned_data["father_employment"]
            father_income  = form.cleaned_data["father_income"]
            # mother details
            mother_full_name =  form.cleaned_data["mother_full_name"]
            mother_address = form.cleaned_data["mother_address"]
            m_phone_number =  form.cleaned_data["m_phone_number"]
            mother_employment = form.cleaned_data["mother_employment"]
            mother_income  = form.cleaned_data["mother_income"]
            # GUARDIAN details
            guardian_full_name =  form.cleaned_data["guardian_full_name"]
            guardian_address = form.cleaned_data["guardian_address"]
            g_phone_number =  form.cleaned_data["g_phone_number"]
            guardian_employment = form.cleaned_data["guardian_employment"]
            guardian_income  = form.cleaned_data["guardian_income"]
            form.save()
            return HttpResponse("THANKS FOR YOUR COOPERATION. REMEMBER ANY FALSE INFROMATION CAN RESULT INTO FAULURE TO FUNDS ALLOCATION")
    else:
        form = FamilyForm() 
        
    context = {
        "form":form,
    }    
       
    return render(request, "home/family.html", context)

def logout_auth(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect("home")