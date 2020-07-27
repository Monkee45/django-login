from django.urls import path, re_path
from users import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    re_path('^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]

    # re_path(r'^login/$', auth_views.login, {'template_name': 'users/login.html'}, name='login'),
