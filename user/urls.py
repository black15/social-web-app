from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from .views import *

app_name = 'user'

urlpatterns = [
   path("dashboard/", dashboard_view, name="dashboard"),
   path("login/", login_view, name="login"),
   path("register/", register_view, name="register"),
   path("logout/", auth_views.LogoutView.as_view(), name="logout"),
   path("password_change/", auth_views.PasswordChangeView.as_view(template_name='password/password_change_form.html',success_url=reverse_lazy('user:password_change_done')), name="password_change"),
   path("password_change_done/", auth_views.PasswordChangeDoneView.as_view(template_name='password/password_changed.html'), name="password_change_done"),
]
