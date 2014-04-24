from django.shortcuts import render


def index(request):
    return render(request, 'quotation/index.html')


def register(request):
    return render(request, 'quotation/register.html')

