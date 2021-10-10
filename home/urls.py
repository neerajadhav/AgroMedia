from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('home/', views.home, name='home'),
    path('liked/', views.like_unlike_post, name='liked'),
    path('newspaper/', views.newspaper, name='newspaper'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('notifications/', views.invited_received_view, name='notifications'),
    # path('all-profiles/', views.profile_list_view, name='all-profiles'),
    path('invite-profiles/', views.invite_profile_list_view, name='invite-profiles'),
    path('profile/', views.profile, name='profile'),
    path('all-profiles/', ProfileListView.as_view(), name='all-profiles'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
]