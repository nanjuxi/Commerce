from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.forms import widgets
from django.forms import fields
from django.utils.safestring import mark_safe
from .models import *

def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


class ProductForm(forms.Form):
    objectName = forms.CharField(max_length=100, widget=widgets.TextInput(attrs={'class':'form-control'}), label=mark_safe("objectName"))
    description = forms.CharField(max_length=2000, widget=widgets.Textarea(attrs={'class':'form-control'}), label=mark_safe("description"))
    startBid = forms.FloatField(widget=widgets.NumberInput(attrs={'class':'form-control'}), label=mark_safe("startBid"))
    image = forms.ImageField(widget=widgets.FileInput(attrs={'class':'form-control'}), label=mark_safe("image"))
    c = [ (1,'food'), (2,'cloth'), (3,'furniture'), (4,'other'), ]
    Select = forms.IntegerField(widget=forms.Select(choices=c, attrs={'class':'form-control'}))




def create(request):
    return render(request, "auctions/create.html", {
        "form": ProductForm()
    })

def get(request):
    form = ProductForm(request.GET)
    objectName = request.GET.get("objectName")
    description = request.GET.get("description")
    startBid = request.GET.get("startBid")
    image = request.GET.get("image")
    Select = request.GET.get("Select")
    f = Product(objectName=objectName, description=description, startBid=startBid,
                image=image, Select=Select)
    f.save()
    return render(request, "auctions/index.html", {
        "form": form
    })








