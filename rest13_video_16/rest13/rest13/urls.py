
from django.contrib import admin
from django.urls import path,include
from firstapp import views
from rest_framework.routers import DefaultRouter

# crating router object
router = DefaultRouter()
# register Studentviewset with router
router.register('studentapiii', views.StudentViewset, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
