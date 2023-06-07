from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import (authenticate,
                                 login,
                                 logout,
                                 update_session_auth_hash
                                 )
from django.contrib.auth.decorators import login_required
from django.utils.encoding import (force_bytes,
                                   force_text,
                                   DjangoUnicodeDecodeError
                                   )
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from django.utils.datastructures import MultiValueDictKeyError
# from .utils import token_generator


@login_required()
def index(request):
    """
        this view renders the profile page of a logged in user
    """
    template_name = 'account/profile.html'
    user = request.user
    context = {'user': user}
    return render(request, template_name, context)


class RegistrationView(View):
    '''
        this view shows the registration form and enables user to
        register an account
    '''
    def get(self, request):
        context = {}
        template_name = 'account/register.html'
        return render(request, template_name, context)

    def post(self, request):
        pass


class LoginView(View):
    '''
        this view shows the login form and enables
        a registered user to login the system
    '''
    def get(self, request):
        context = {}
        template_name = 'account/login.html'
        return render(request, template_name, context)

    def post(self, request):
        pass


def logout_page(request):
    '''
        This view displays a modal for confirmation
        if a user wishes to log out.
    '''
    logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('home')
