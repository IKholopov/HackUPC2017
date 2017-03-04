from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^logout$', views.logout, name='logout'),
    url('', include('social_django.urls', namespace='social'))
]
