import json
from os import stat
from re import L
from urllib import response
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# Model object - single Student Data

''' Below methods studentdetails and list are called serialization'''
''' i.e we are extracting object and the converting it into JSON data (complex to parsed)'''

def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    print( stu)
    serializer = StudentSerializer(stu)
    print( serializer)
    print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data)

    
# Query SET i.e getting all the objects
def student_list(request):
    stu = Student.objects.all()
    print( stu)
    serializer = StudentSerializer(stu, many=True)
    print( serializer)
    print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe=False) # here we need to write safe = false bcoz it returns list and not dict
       # instead of writing jsondata and returning httprespone dirrectly return this

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializer = StudentSerializer(data = python_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            print(json_data)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')





# def student_update(request, pk):
#     stu = Student.objects.get(id = pk)
#     serializer = StudentSerializer(stu, data=request.data)
#     if serializer.is_valid():
#         serializer.save()

