from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermission import MyPermission

#  http http://127.0.0.1:8000/studentapi/ 'Authorization:Token feed133c2171ef7a86393af4ad6edb10c1428bba '
# token authentications 

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    # if we do not use this two line then we access data withour authorize.
    #  http http://127.0.0.1:8000/studentapi/ just used But
    
    # use two line requeired user token
    # http http://127.0.0.1:8000/studentapi/ 'Authorization:Token feed133c2171ef7a86393af4ad6edb10c1428bba '
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
# for post request from command line 
#  http -f POST http://127.0.0.1:8000/studentapi/ name=raju roll=103 city=kushtia 'Authorizati

# delete 
# http DELETE http://127.0.0.1:8000/studentapi/2/ 'Authorization:Token feed133c2171ef7a86393af4ad6edb10c1428bba'

# for put operation
#  http PUT  http://127.0.0.1:8000/studentapi/3/ name=raju roll=104 city=kushtia 'Authorization:Token feed133c2171ef7a86393af4ad6edb10c1428bba'