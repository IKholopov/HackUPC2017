from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
import bestin.services as services

class IndexView(TemplateView):
    template_name="index.html"

def test(request):
    services.analyze_feed(request.user.social_auth.get())
    return HttpResponseRedirect('/')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
