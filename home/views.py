from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .forms import PersonalForm
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
            print(name)
            print(DATE_OF_BIRTH)
            print(ID_NO_passport)
    else:
     form = PersonalForm()
    
    return render(request, "home/home.html", {'form': form})


# polling form
def polling(request):
    return render(request, "home/polling.html")

# family form
def family(request):
    return render(request, "home/family.html")

def logout(request):
    logout(request)
    return redirect("login")