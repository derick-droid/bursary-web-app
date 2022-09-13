from django.shortcuts import render

#welcome login page
def index(request):
    return render(request, "index.html")

# home page
def home(request):
    return render(request, "home.html")

# sign page
def sign(request):
    return render(request, "sign.html")

# login page
def login(request):
    return render(request, "login.html")

# polling form
def polling(request):
    return render(request, "polling.html")

# family form
def family(request):
    return render(request, "family.html")