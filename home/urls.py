from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('liked/', views.like_unlike_post, name='liked'),
    path('newspaper/', views.newspaper, name='newspaper'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
]