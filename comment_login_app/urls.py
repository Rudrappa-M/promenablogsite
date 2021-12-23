from django.urls import path

from comment_login_app import views
from comment_login_app.views import *

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


urlpatterns = [
    path('Login_List/',views.Login_List),
    path('Login_page/', views.User_Login),
    path('Token_Cookie/',views.Token_Cookie),
    path('View_User/', views.View_User),
]
