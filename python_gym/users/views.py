from base64 import urlsafe_b64decode, urlsafe_b64encode
import base64
from pyexpat.errors import messages
from django.shortcuts import redirect, render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import EmailWhiteList
from users.models import CustomUser

from users.tokens import AccountActivationTokenGenerator
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from users.tokens import account_activation_token
from django.utils.encoding import force_str
from django.contrib.sites.shortcuts import get_current_site


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        r = EmailWhiteList.objects.filter(Email=username)
        if r.count()==0:
            messages.info(
                request, 'Email not registered with the admin')
        else:
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.info(
                    request, 'Try again! username or password is incorrect')

    context = {}
    return render(request, 'user/login.html', context)


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            user = f.save()
            # user.refresh_from_db()
            print(user)
            # messages.success(request, 'Account created successfully')
            # return redirect('login')
            try:
                current_site = get_current_site(request)
                print(current_site.domain)
                subject = 'Please Activate Your Account'
                # load a template like get_template()
                # and calls its render() method immediately.
                message = render_to_string('user/activation_request.html', {
                    'user': user,
                    'domain': current_site.domain,
                    # 'uid': urlsafe_b64encode(force_bytes(user.id)),
                    'uid': user.id,
                    # method will generate a hash value with user related data
                    'token': account_activation_token.make_token(user),
                })
                print(message)
                user.email_user(subject, message)
                return redirect('activation_sent')
            except Exception as e:
                print(e)
    else:
        f = CustomUserCreationForm()

    return render(request, 'user/register.html', {'form': f})


def logout(request):
    auth_logout(request)
    # messages.info(request, "You have successfully logged out.")
    return redirect("login")
    # resp = auth_logout()
    # resp['Refresh'] = '3;URL=/login/' # redirects after 3 seconds to /account/login
    # return resp


def activation_sent_view(request):
    return render(request, 'user/activation_sent.html')


def activate(request, uidb64, token):
    print(uidb64)
    print(token)
    try:
        # uid = force_str(urlsafe_base64_decode(uidb64))
        print('inside try')
        # uid = urlsafe_b64decode(uidb64).decode()
        # uid = base64.urlsafe_b64decode(uidb64)
        uid = uidb64
        print(uid)
        user = CustomUser.objects.get(id=uid)
        print(user)
    # except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
    #     user = None
    except Exception as e:
        print(e)
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.signup_confirmation = True
        user.save()
        auth_login(request, user)
        return redirect('index')
    else:
        return render(request, 'user/activation_invalid.html')
