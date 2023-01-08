from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
# Model Object - Single Student Data


def student_detail(request,pk):
    stu = Student.objects.get(id=pk) # it is a complex data which convert into python data in line 9
    # print(stu)# output Student object (1)
    serializer = StudentSerializer(stu) # it is a python data or python dictionary which converted into json data in next line
    # print(serializer)#output StudentSerializer(<Student: Student object (1)>):
                                              # name = CharField(max_length=100)
                                              # roll = IntegerField()
                                              # city = CharField(max_length=100)

    # print(serializer.data)#output {'name': 'aman', 'roll': 23, 'city': 'ranhi'}


    # json_data = JSONRenderer().render(serializer.data) # it is a json data and then we will send json data in frontend using http or something alse
    # print(json_data) #output {"name":"aman","roll":23,"city":"ranhi"}'

    # return HttpResponse(json_data,content_type='application/json')
    # instead of writing tow lines 22,25 we can use a line for a execute
    return JsonResponse(serializer.data)

# Query set -All Student Data
def student_list(request):
    stu = Student.objects.all()# it is a complex data which convert into python data in line 9
    # print(stu)# output Student object (1)
    serializer = StudentSerializer(stu,many=True) # it is a python data or python dictionary which converted into json data in next line
    # print(serializer)#output StudentSerializer(<Student: Student object (1)>):
                                              # name = CharField(max_length=100)
                                              # roll = IntegerField()
                                              # city = CharField(max_length=100)

    # print(serializer.data)#output {'name': 'aman', 'roll': 23, 'city': 'ranhi'}


    json_data = JSONRenderer().render(serializer.data) # it is a json data and then we will send json data in frontend using http or something alse
    # print(json_data)#output {"name":"aman","roll":23,"city":"ranhi"}'

    return HttpResponse(json_data,content_type='application/json')
    
    
    
# using ModelViewset in rest framework and with this three line we can do crud operation....
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class =StudentSerializer
    queryset= Student.objects.all()