from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.

def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    # Json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(Json_data, content_type='application/json')
    return JsonResponse(serializer.data)


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    
    # below two line for return json data httpresponse form 
    # Json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(Json_data, content_type='application/json')
    
    # JsonTesponse instead of above to line.
    return JsonResponse(serializer.data, safe=False)
