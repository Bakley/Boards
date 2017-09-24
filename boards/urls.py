from django.conf.urls import url

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.boards_topic, name='boards_topic'),
]
