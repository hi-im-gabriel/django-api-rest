from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import TodoList
from .serializers import TodoListSerializer

class TodoListCollection(APIView):
    def get(self, request):
        items = TodoList.objects.all()
        serializer = TodoListSerializer(items, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TodoListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoListDetail(APIView):
    def delete(self, request, id):
        item = TodoList.objects.get(id=id)
        item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        item = TodoList.objects.get(id=id)
        serializer = TodoListSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

