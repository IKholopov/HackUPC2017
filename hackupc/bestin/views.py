from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect

class IndexView(TemplateView):
    template_name="index.html"

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
