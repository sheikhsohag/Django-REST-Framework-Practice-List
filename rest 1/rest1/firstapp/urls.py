from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:pk>', views.student_detail, name='student_detail'),
    path('student_list/', views.student_list, name='student_list'),
]
