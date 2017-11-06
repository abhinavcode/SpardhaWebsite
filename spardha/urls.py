from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^register/', views.register, name='register'),
    url(r'^ourteam/', views.team, name='team'),
    url(r'^confirmation', views.regconfirm, name='confirmation'),
    url(r'^adminlogin', views.adminlogin, name='adminlogin'),
    url(r'^adminfixtures', views.fixturesandresult, name='adminfixtures'),
    url(r'^adminresults', views.results, name='adminresults'),
    url(r'^admin1', views.admin, name='admin'),
    url(r'^login', views.teamlogin, name='teamlogin'),
    url(r'^user', views.user, name='user'),
    url(r'^adminlogout', views.adminlogout, name='adminlogout'),
    url(r'^logout', views.userlogout, name='logout'),
    url(r'^adminteam', views.ourteam, name='adminteam'),
    url(r'^games', views.usergames, name='usergames'),
    url(r'^adminevents', views.adminevents, name='adminevents'),
    url(r'^college/(?P<num>[0-9]+)/$', views.collegedesc, name='collegedesc'),
    url(r'^events/', views.events, name='events'),
    url(r'^badmintonschedule/', views.badsc, name='badmintonschedule'),

]
