from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.


#apiview allow as to make api in a small line of code


# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello World'})
    
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})


# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#      print(request.data)
#      return Response({'msg':'This is post request'})

# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == 'GET':
#          return Response({'msg':'This is get request'})
#     if request.method == "POST":
#      print(request.data)
#      return Response({'msg':'This is post request','data':request.data})



#CRUD Operation using apiview

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if  request.method =='GET':
       id= request.data.get("id")
       if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
       stu = Student.objects.all()
       serializer = StudentSerializer(stu,many =True)
       return Response(serializer.data)
   
   ## #incase if u want to run in brower
# def student_api(request,pk):
#     if  request.method =='GET':
#        id = pk
#        if id is not None:
#             stu = Student.objects.get(id=pk)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#        stu = Student.objects.all()
#        serializer = StudentSerializer(stu,many =True)
#        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    
  
    if request.method=='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

            

   # using request.data and Response we r  able to perform crud using less no. of code  
            
    if request.method == 'PUT':
        id = request.data.get("id")
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
        
    
        
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})