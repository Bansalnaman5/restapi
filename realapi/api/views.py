from rest_framework.response import Response
from api import serializers,models
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView)
# # RetrieveUpdateAPIView accepts patch request with the parameter to be updated otherwise get request is also supported
# ListCreateAPIView accepts post request with a body to register or create a new entity or article here otherwise returns all the articles in get request




class Articlelistview(ListAPIView):   #  ListCreateAPIView
    serializer_class=serializers.ArticleSerializer
    queryset=models.Article.objects.all()

    def get_queryset(self):
        query={}
        for key,value in self.request.GET.items():
            query["{}__icontains".format(key)]=value
        return models.Article.objects.filter(**query)

       # return models.Article.objects.all()    #super().get_queryset()

    # def post(self,request):
    #     return Response(request.body)
    #it is hashed because we need the query set to be refreshed on every call and not want cached data of the previous query


class Articledetailview(RetrieveAPIView):  #RetrieveUpdateAPIView
    serializer_class=serializers.ArticleSerializer
    queryset=models.Article.objects.all()



# function based views  
# class Student:
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.roll=roll
#         self.marks=marks

# @api_view()
# def userApi(request):
#     s1=Student('naman',1,100)
#     s2=Student('mummy',2,99)
#     s3=Student('bhanu',3,98)
#     response=serializers.StudentSerializer([s1,s2,s3],many=True)

#     return Response(response.data)


# @api_view()
# def articleApi(request):
#     article=models.Article.objects.all()
#     response=serializers.ArticleSerializer(article,many=True)
#     return Response(response.data)

# @api_view(['POST'])
# def createArticleApi(request):
#     body=json.loads(request.body)
#     response=serializers.ArticleSerializer(data=body)
#     if response.is_valid():
#         inst=response.save()
#         response=serializers.ArticleSerializer(inst)
#         return Response(response.data)
#     return Response(response.errors)

# @api_view(['POST'])
# def createUserApi(request):
#     print(request.body)
#     import io
#     stream=io.BytesIO(request.body)
#     parsed=JSONParser.parse(stream)
#     data=serializers.StudentSerializer(data=parsed)
#     print(data.is_valid())
#     print(data.validated_data)
#     return Response({'message':'Hello'})