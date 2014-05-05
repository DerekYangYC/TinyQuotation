from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response


def index(request):
    return render(request, 'quotation/index.html')


def register_form(request):
    return render(request, 'quotation/register.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user = User.objects.create_user(username=form['username'], password=form['password'],
                                        email=form['email'])
        user.save()
        
        return render_to_response('quotation/index.html')

