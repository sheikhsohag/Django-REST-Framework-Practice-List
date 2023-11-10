
from django.contrib import admin
from django.urls import path,include
from firstapp import views
from rest_framework.routers import DefaultRouter
# auto token create korar jonno
#  http POST http://127.0.0.1:8000/gettoken/ username="sohag" password="123"
# command line and serverrun 
from rest_framework.authtoken.views import obtain_auth_token



router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', obtain_auth_token),
]
