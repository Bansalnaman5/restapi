from django.urls import path
from api import views

urlpatterns=[
    #path('users/',views.userApi),
    path('articles/',views.Articlelistview.as_view()),
    path('articles/<int:pk>',views.Articledetailview.as_view()),
    
    #path('create_article/',views.createArticleApi)
]