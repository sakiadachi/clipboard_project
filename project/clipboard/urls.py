from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clipboards', views.ClipboardViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
