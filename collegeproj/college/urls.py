from django.urls import path
from .views import Add_college, List_college, Detail_college, Update_college, Delete_college

urlpatterns = [
    path('add/', Add_college.as_view()),
    path('list/', List_college.as_view()),
    path('detail/<int:pk>/', Detail_college.as_view()),
    path('update/<int:pk>/', Update_college.as_view()),
    path('delete/<int:pk>/', Delete_college.as_view()),
]
