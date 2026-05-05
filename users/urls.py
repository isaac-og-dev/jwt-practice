from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'teachers', TeacherViewSet, basename='teachers')

urlpatterns = [
    path('', include(router.urls)),
]