# Create your views here.
from django.contrib.auth import logout
from django.http import  HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from Allthink.forms import *


def user_page(request, username):
    user = get_object_or_404(User, username=username)
    variables = RequestContext(request, {
        'username': username,
    })

    return  render_to_response('user_page.html', variables)

def main_page(request):
    return render_to_response(
        'main_page.html', RequestContext(request)
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html',variables)
