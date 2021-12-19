from django.contrib import admin
from django.urls import path, include
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist.urls'))
]
