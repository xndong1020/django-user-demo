from django.contrib.auth.views import LoginView, LogoutView


class LoginView(LoginView):
    template_name = 'accounts/login.html'


class LogoutView(LogoutView):
    template_name = 'accounts/login.html'
    next_page = '/accounts/login'