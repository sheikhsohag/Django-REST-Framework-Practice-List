from django.contrib import admin
from django.urls import path,include
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.ListCreateStudentAPI.as_view()),
    # path('studentapi/',views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>',views.StudentRetrieve.as_view()),
    #  path('studentapi/<int:pk>',views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentAPI.as_view()),
    path('studentapi/<int:pk>',views.Retrieve_Updata_createStudentAPI.as_view()),
]
