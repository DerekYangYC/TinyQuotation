from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.template import RequestContext


def index(request):
    return render(request, 'quotation/index.html')


def register_form(request):
    return render(request, 'quotation/register.html')


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                        email=request.POST['email'])
        user.save()

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        auth.login(request, user)

        return render_to_response('quotation/index.html', context_instance=RequestContext(request))


def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return render_to_response('quotation/index.html')


