from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .forms import PersonalForm, PollingForm
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
     
        #  messages.error(request, "An error occurred while creating the account ")
        

    return render(request, "home/sign.html")


# login page
def login_auth(request):

    if request.method == "POST":
        username= request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            # messages.success(request, "You are logged in successfully")
            return redirect("home")
        else:
            # messages.error(request, "Error in loggin in")
            return redirect( "login")
    else:
        return render(request, "home/login.html")
    
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
            # favorite_fruit = form.cleaned_data["favorite_fruit"]
            print(name)
            print(DATE_OF_BIRTH)
            print(ID_NO_passport)
            print(gender)
            # print(favorite_fruit)
            print(school)
            print(admission_number)
            print(campus_branch)
            print(faculty_branch)
            print(course_study)
            print(mode_study)
            print(class_year)
            print(course_duration)
            print(year_completion)
            print(phone_number )
    else:
     form = PersonalForm()
    
    return render(request, "home/home.html", {'form': form})


# polling form
def polling(request):
    
    if request.method == "POST":
        form = PollingForm(request.POST)
        
        if form.is_valid:
            ward = form.cleaned_data["ward"]
            location = form.cleaned_data["location"]
            sub_location =  form.cleaned_data["sub_location"]
            physical_address =  form.cleaned_data["physical_address"]
            permanent_address =  form.cleaned_data["permanent_address"]
            institution_post_address =  form.cleaned_data["institution_post_address"]
            institution_tel_phone  = form.cleaned_data["institution_tel_phone"]
            amount_applied = form.cleaned_data["amount_applied"]
            print(physical_address)
            print(permanent_address)
            print(amount_applied)
            print(institution_tel_phone)
            print(institution_post_address)
            print(location)
            print(ward)
            print(sub_location)
            
    else:
        form = PollingForm()
    
    return render(request, "home/polling.html", {"form":form})

# family form
def family(request):
    return render(request, "home/family.html")

def logout(request):
    logout(request)
    return redirect("login")