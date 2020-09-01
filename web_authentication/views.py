from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic import View, UpdateView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUser_Login_Form

from api_notifications.models import Notification
from api_configurations.models import Configuration
from api_spaces.models import Space

from django.template.loader import render_to_string
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your views here.
class CreateUser_View(View):
    template_name = "web_authentication/signup.html"

    def get(self, request, *args, **kwargs):
        isErrorMessage = False
        errorMessage = ""

        user_form = CreateUser_Login_Form()
        context = {"user_form": user_form, "registered": False, "isErrorMessage": isErrorMessage, "errorMessage": errorMessage}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        isErrorMessage = False
        errorMessage = ""
        registered = False

        user_form = CreateUser_Login_Form(request.POST)
        if user_form.is_valid():
            user = user_form.save()

            configurations = Configuration.objects.all()
            configuration = configurations.first()
            Notification.add_notification(notify_user=user, source_user=user, message="Welcome to the " + configuration.organization_name + " website!")
            registered = True

            # Create user space
            space_title = title=user.first_name + " " + user.last_name
            space = Space(title=space_title, summary=space_title, body=space_title, show_application_menu=False, show_space_menu=True, \
                            status='INACTIVE', admin_method='USER', admin_user=user, user_space=True, system_space=True)
            space.save()
        else:
            isErrorMessage = True
            errorMessage = user_form.errors
        context = {"user_form": user_form, "registered": registered, "isErrorMessage": isErrorMessage, "errorMessage": errorMessage}
        return render(request, self.template_name, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

class PasswordChangedView(TemplateView):
    template_name = 'web_authentication/password_changed.html'
