from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

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
         return redirect("index")

     return render(request, "home/sign.html")

# login page
def login(request):
    return render(request, "home/login.html")

# polling form
def polling(request):
    return render(request, "home/polling.html")

# family form
def family(request):
    return render(request, "home/family.html")