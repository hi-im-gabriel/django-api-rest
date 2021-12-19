from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListCollection.as_view()),
    path('<int:id>', views.TodoListDetail.as_view())
]
