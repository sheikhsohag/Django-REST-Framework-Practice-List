from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST','GET'])
def hello_world(request):
    if request.method == 'GET':
        print(request.data)
        return Response({'msg':'get hellow world'})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'post hellow world', 'data':request.data})
