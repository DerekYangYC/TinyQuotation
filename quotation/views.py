from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext


def index(request):
    return render_to_response(request, 'quotation/index.html')


def register(request):
    return render_to_response(request, 'quotation/register.html')


def register_submit(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                        email=request.POST['email'])
        user.save()

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        auth.login(request, user)

        # return render_to_response('quotation/index.html', context_instance=RequestContext(request))
        # return redirect('quotation/index.html')
        return redirect('/quotation/')


def login(request):
    return render_to_response(request, 'quotation/login.html')


def login_submit(request):
    print("haha")
    if request.method == 'POST':
        print("in post")
        print(request.POST['username'])
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        print(request.POST['username'])
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/quotation/')
        else:
            return redirect('/quotation/login/', RequestContext({'isLogin': '1'}))


def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
        # return render_to_response('quotation/index.html')
        return redirect('/quotation/')

