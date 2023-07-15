from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('editar_perfil/', UserEditView.as_view(), name="editar-perfil"),
    #path('<int:pk>/password/', auth_views.PasswordChangeView.as_view(template_name="registration/cambiar_contraseña.html")),
    path('<int:pk>/password/', PasswordsChangeView.as_view(template_name="registration/cambiar_contraseña.html")),
    path('password_success', views.password_success, name="password_success"),

]
