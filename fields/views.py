from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,template_name="signup.html")

def login(request):
    return render(request, template_name="login.html")

def dashboard(request):
    return render(request,template_name="dashboard.html")

def blog(request):
    return render(request, template_name="blog.html")
def myblog(request):
    return render(request, template_name="myblog.html")
def adminn(request):
    return render(request, template_name="admin.html")