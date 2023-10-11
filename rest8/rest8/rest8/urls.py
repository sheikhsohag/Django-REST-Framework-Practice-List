from django.contrib import admin
from django.urls import path,include
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.student_api, name="studentapi"),
    path('studentapi/<int:pk>',views.student_api, name="studentapi"),
]
