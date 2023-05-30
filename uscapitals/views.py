import json
import re
from json import dumps
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import UpdateView


class USCapitalView(TemplateView):
    template_name =  'uscapitals/uscapital.html'

class KeepGoingView(TemplateView):
    template_name =  'uscapitals/keepgoing.html'

class successView(TemplateView):
    template_name =  'uscapitals/success.html'

class USCapsView(TemplateView):
    template_name =  'uscapitals/uscaps.html'

