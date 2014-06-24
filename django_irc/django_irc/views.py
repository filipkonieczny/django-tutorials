from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


# home page view
def homepage(request):
    '''
    '''

    return render_to_response('homepage.html')


# loggin in
def login_user(request):
    c = {}
    c.update(csrf(request))

    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)


    if user is not None:
        auth.login(request, user)

        return HttpResponseRedirect('/login/win')

    else:
        return HttpResponseRedirect('/login/fail')


def logged_in(request):
    # return HttpResponseRedirect('/djirc/',
    #                             {'full_name': request.user.username})
    return HttpResponseRedirect('/djirc/')
    # return render_to_response('djirc.html',
    #                           {'username': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)

    return render_to_response('logout.html')



# register
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return render_to_response('register_success.html')

        else:
            return render_to_response('register_fail.html')


    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('register.html', args)