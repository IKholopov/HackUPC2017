from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^test$', views.test, name='test'),
    url(r'^geodata$', views.geodata, name='geodata'),
    url(r'^userscore$', views.get_user_score, name='userscore'),
    url(r'^topscore$', views.get_top_scores, name='topscore'),
    url(r'^loading', views.Loading.as_view()),
    url(r'^loadposts', views.load_posts, name="loadposts"),
    url('', include('social_django.urls', namespace='social'))
]
