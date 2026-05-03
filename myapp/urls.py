from django.contrib import admin
from django.urls import path, include

#JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/1.0/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #lista de usuarios
    path('api/1.0/', include('users.urls')),
]
