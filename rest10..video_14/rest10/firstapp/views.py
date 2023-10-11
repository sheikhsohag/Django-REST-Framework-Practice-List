from .models import Student 
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin


class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)