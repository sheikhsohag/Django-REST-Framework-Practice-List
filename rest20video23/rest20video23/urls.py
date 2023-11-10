
from django.contrib import admin
from django.urls import path,include
from firstapp import views
from rest_framework.routers import DefaultRouter
# extend of previous
# auto token create
from rest_framework.authtoken.views import obtain_auth_token
from firstapp.auth import CustomAuthToken



router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', CustomAuthToken.as_view(),name="gettoken"),
]
