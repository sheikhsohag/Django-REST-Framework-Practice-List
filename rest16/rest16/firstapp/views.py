from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    # # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # # permission_classes = [IsAdminUser]
    # # permission_classes = [IsAuthenticatedOrReadOnly]
    # # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    
