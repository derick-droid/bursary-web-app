from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login


#welcome login page
def index(request):
    return render(request, "home/index.html")

# home page
def home(request):
    return render(request, "home/home.html")

# sign page
def sign(request):
    
    
     if request.method == "POST":
         full_name = request.POST["name"]
         email = request.POST["email"]
         password = request.POST["password"]
         confirm_password = request.POST["password2"]
         
         my_user = User.objects.create_user(full_name,email,password)
         my_user.save()
         
         messages.success(request, "Account created successfully ")
         return redirect("home")
     
     messages.error(request, "An error occurred while creating the account ")
        

     return render(request, "home/sign.html")


# login page
def login(request):
    if request.method == "POST":
        email = email.request.POST["email"]
        password = password.request.POST["password"]
        user = authenticate("email = email", "password = password")
        
        if user is not None:
            login(request, user)
            messages.success(request, f"You are logged in successfully")
            return redirect("home")
        else:
            messages.error(request, "Error in loggin in")
            return redirect (request, "login")
    return render(request, "home/login.html")

# polling form
def polling(request):
    return render(request, "home/polling.html")

# family form
def family(request):
    return render(request, "home/family.html")