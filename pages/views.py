from operator import itemgetter
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
from users.forms import CustomUserChangeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from json import dumps


class HomePageView(TemplateView):
    template_name =  'pages/home.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


def contact_form(request):
        template_name = 'pages/contact_us.html'
        form = ContactForm()
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = f'message from {form.cleaned_data["email"]}'
                message = f'Name: {form.cleaned_data["name"]} \n Message: \n {form.cleaned_data["message"]}'
                sender = ['smith010123@gmail.com']
                from_email = ['smith010123@gmail.com']
                recipients = ['smith010123@gmail.com']
                try:
                    send_mail(subject,message,sender,from_email,recipients)
                except BadHeaderError:
                    return HttpResponse('Invalid header found')
                return HttpResponse('Form Submitted, Thank you.')
        return render(request, 'pages/contact_us.html', {'form':form})


class LoginView(TemplateView):
    template_name = 'pages/login.html'

class devView(TemplateView):
    template_name = 'pages/dev.html'

class Random_AceView(TemplateView):
    template_name = 'pages/Random_Ace.html'

class Random_Ace_GainView(TemplateView):
    template_name = 'pages/Random_Ace_Gain.html'

class Random_Ace_LoseView(TemplateView):
    template_name = 'pages/Random_Ace_Lose.html'



