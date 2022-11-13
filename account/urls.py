from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view

app_name = __name__

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register')
]
