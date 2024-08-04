from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "register.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})


def login(request):
    print(request.GET.get("next"), "THIS IS NEXT")
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            next_url = request.POST.get("next")
            print("this is next_url", next_url, "d")
            return redirect(next_url or "quiz_list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("quiz_list")
