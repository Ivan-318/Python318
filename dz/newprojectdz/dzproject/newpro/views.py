from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    psw = 'qwerty'
    return render(request, "newpro/home.html", {'password': psw, 'title': "Домашнее задание"})
