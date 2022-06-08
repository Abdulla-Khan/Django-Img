from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from Todo.serializers import TodoSerializer
from Todo.models import Todo
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

# Create your views here.


class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ImageView(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
