from django.shortcuts import render


def index(request):
    return render(request,'home/index.html')


def drunkwiz(request):
    return render(request,'home/drunkwiz.html')