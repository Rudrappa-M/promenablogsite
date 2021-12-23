from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Newsletter import views

router=DefaultRouter()

router.register('post_Subscribe',views.post_Subscribe)
router.register('post_newsletter',views.post_newsletter)

urlpatterns = [
    path('',include(router.urls)),
    path('post_newsletter<int:my_id>/',views.post_newsletter.as_view),
    path('post_Subscribe<int:my_id>/',views.post_Subscribe.as_view),

]