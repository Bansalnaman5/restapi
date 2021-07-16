from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import models,serializers
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView    
)

class Studenlistview(ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializers
class Studentdetailview(RetrieveUpdateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializers

#deleting entry

class Studentdeleteview(DestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializers