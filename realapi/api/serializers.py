from rest_framework import serializers
from api import models
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    marks=serializers.IntegerField()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields='__all__'
        

class ArticleSerializer(serializers.ModelSerializer):
    taglist=TagSerializer(many=True,read_only=True)
    class Meta:
        model=models.Article
        fields='__all__'
    
    def create(self,validated_data):
        # print("chal chal apna kam kar")
        # return super().create(*args,**kwargs)
        return self.Meta.model.objects.create(**validated_data)