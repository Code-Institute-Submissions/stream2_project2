from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User, Group

# Create your views here.

def show_index(request):
    if request.user.is_authenticated:
        return redirect("read_posts")
    else:    
        return render(request, "index.html")



def signup(request):
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user 
            profile.save()
            
            if "type" in request.GET:
                group = Group.objects.get(name=request.GET["type"])
                group.user_set.add(user)
            
            username = user_form.cleaned_data.get("username")
            raw_password = user_form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("read_posts")
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
        return render(request, "registration/signup.html", {"user_form": user_form, "profile_form": profile_form})



def my_profile(request):
    group = request.user.groups.all()[0]
    return render(request, "profile.html", {"group": group})