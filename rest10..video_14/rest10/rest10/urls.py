from django.contrib import admin
from django.urls import path,include
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentAPI.as_view()),
    path('studentapi/<int:pk>/',views.StudentAPI.as_view()),
]