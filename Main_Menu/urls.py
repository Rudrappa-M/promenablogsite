from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from Main_Menu import views
from Main_Menu.views import GenericAPIView

# router=DefaultRouter()
# router.register('mainmenu', views.RetriveData)
# router.register('category',views.createCategeory)

urlpatterns = [
    # path('', include(router.urls)),
    # path('create_menu<int:my_id>/', views.createmenu.as_view),
    path('create_category/<int:pk>/',views.CreateRetrieve.as_view()),
    path('Main_Menu/<int:pk>/',views.RetriveData.as_view()),
    path('Main_Menu/',views.Retrivelist.as_view()),
    path('create_category/',views.CreateRetrivelist.as_view()),



]