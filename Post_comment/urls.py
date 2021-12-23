from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Post_comment import views


router = DefaultRouter()
# router.register('BlogPost', views.BlogPost)
router.register('CommentModel', views.CommentModel)
router.register('ReplyModel', views.ReplyModel)


urlpatterns = [
    path('', include(router.urls)),
    path('BlogPost/<int:pk>/', views.RetriveData.as_view()),
    path('BlogPost/', views.Retrivelist.as_view()),
    path('CommentModel<int:my_id>/', views.CommentModel.as_view),
    path('ReplyModel<int:my_id>/', views.ReplyModel.as_view),
]
