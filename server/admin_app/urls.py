from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="signin"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('profile', views.profile, name="profile"),
    path('delete', views.delete, name="delete"),
    path('logout', views.logout, name="logout"),
]
