from django.shortcuts import render, render_to_response


def index(request):
    return render(request, 'quotation/index.html')


def register_form(request):
    return render(request, 'quotation/register.html')


def register(request):
    if request.method == 'POST':
        print(request.POST['username'] + " , " + request.POST['password'] + " , " + request.POST['realname'] + " , " +
              request.POST['email'])
        return render_to_response('quotation/index.html')

