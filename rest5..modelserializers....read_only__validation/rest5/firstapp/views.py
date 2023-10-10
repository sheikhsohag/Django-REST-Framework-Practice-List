from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt




# from django.utils.decorators import method_decorator
# from django.views import View
# class ar age likhte hobe..
# @method_decorator(csrf_exempt, name='dispatch')
# class Studentapi(View):
#     def get(self, requenst, *args, **kwarge):
#         ar pore first if ar pore copy kore boshai dilei hobe
# urls change kore class releted korte hobe

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        steam = io.BytesIO(json_data)
        python_data = JSONParser().parse(steam)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg = {'mgs':'Data Created'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
        

    if request.method == 'PUT':
        json_data = request.body
        stream= io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial= True)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"update completed"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json') 
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        msg = {"msg":"Data Delete"}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json') 
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type = 'application/json')
    
        
        
    
        
        