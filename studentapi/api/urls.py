from django.urls import path
from api import views

urlpatterns=[
    path('students/',views.Studenlistview.as_view()),
    path('students/<int:pk>/',views.Studentdetailview.as_view()),
    path('deletestudent/<int:pk>',views.Studentdeleteview.as_view())
]