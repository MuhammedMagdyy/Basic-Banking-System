from ast import NotEq
from django.forms import ValidationError
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from multiprocessing import context
# from turtle import update
from django.dispatch import receiver
from django.shortcuts import redirect, render
from .models import Profile
from .forms import *
from django.contrib import messages
# Create your views here.


def list_view(request):
    context = {}
    context["dataset"] = Profile.objects.all()
    return render(request, "bank_system/list_view.html", context)


def index_view(request):
    context = {}
    context["dataset"] = Profile.objects.all()
    return render(request, "bank_system/html/index.html", context)


def update_view(request, id):
    context = {}
    context["error"] = ""
    sender = Profile.objects.get(id=id)
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        balance = int(form.cleaned_data['balance'])
        receiver = Profile.objects.filter(email=email)
        if not len(receiver):
            context["error"] = "is must"
            context["email"] = email
            context["balance"] = balance
        else:
            receiver = Profile.objects.filter(email=email)[0]
            if sender.balance >= balance:
                sender.balance = sender.balance - balance
                receiver.balance = receiver.balance + balance
            sender.save()
            receiver.save()
            return HttpResponseRedirect("http://banking1system.herokuapp.com/bank_system/list/")
    context["form"] = form
    return render(request, "bank_system/html/update_view.html", context)
