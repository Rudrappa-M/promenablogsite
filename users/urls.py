from django.urls import path
from .views import RegisterView, LoginView #ChangePasswordView

urlpatterns = [
    path('Register/',RegisterView.as_view()),
    path('Login/',LoginView.as_view()),
    # path('change_password/',ChangePasswordView.as_view())

]
