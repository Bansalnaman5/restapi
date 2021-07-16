from django.db import models

class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Article(models.Model):
    slug=models.SlugField(null=False,blank=False)
    title=models.CharField(max_length=256)
    description=models.TextField()
    body=models.TextField()
    taglist=models.ManyToManyField('Tag',blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)
    favorited=models.BooleanField()
    favoritesCount=models.IntegerField(default=0)

    def __str__(self):
        return self.title





    