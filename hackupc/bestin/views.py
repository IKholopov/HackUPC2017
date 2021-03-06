from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import logout as auth_logout
from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
import bestin.services as services
from bestin.models import Activity
import json
import time

class IndexView(TemplateView):
    template_name="index.html"

class Loading(TemplateView):
    template_name="loading.html"

def load_posts(request):
    services.analyze_feed(request.user)
    return JsonResponse(dict())

def test(request):
    services.analyze_feed(request.user)
    return HttpResponseRedirect('/')

def geodata(request):
    jsonData = serializers.serialize("json", list(Activity.objects.all()), fields=('user_id'))
    return JsonResponse(jsonData, safe=False)

def get_user_score(request):
    return JsonResponse(json.dumps(str(Activity.objects.filter(user_id=request.user).aggregate(Sum('score')))), safe=False)

def get_top_scores(request):
    scores = Activity.objects.select_related('user_id').values('user_id__username').annotate(total_score=Sum('score'))
    highscores = []
    for score in scores:
        print(score)
        highscores.append(score)
    highscores.sort(key=lambda x: x["total_score"])
    return JsonResponse(json.dumps(highscores), safe=False)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
