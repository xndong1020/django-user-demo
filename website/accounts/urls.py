from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='accounts-login'),
    path('logout/', views.LogoutView.as_view(), name='accounts-logout'),
]
