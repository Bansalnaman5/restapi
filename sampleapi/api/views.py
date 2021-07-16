from rest_framework.decorators import api_view
from api import serializers
from rest_framework.response import Response

class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks


@api_view()
def userApi(request):
    # users=[
    #     {
    #         "name":'Naman Bansal',
    #         "language":'python'
    #     },
    #     {
    #         "name":'Meenakshi',
    #         "language":'C++'
    #     }
    # ]
    student1=Student("naman",1 ,100)
    student2=Student("mummy",2 ,99)
    student3=Student("bhanu",3 ,98)
    response=serializers.StudentSerializer([student1,student2,student3],many=True)


    return Response(response.data)
