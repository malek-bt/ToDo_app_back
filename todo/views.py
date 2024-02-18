from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ToDoSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
# Create your views here.

class CreateToDoView(APIView):
   def post(self,request):
      serializer = ToDoSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'message: Task created successfully'} , status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
      

   def get(self , request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos,many=True)
        return Response(serializer.data)
   


   def put(self , request , pk):
      
      try:
         todo = ToDo.objects.get(pk=pk)
      except ToDo.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
      
      serializer = ToDoSerializer(todo , data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'message: Task updated successfully'}, status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
      

   
   
   def delete(self, request):
      try:
         delete_ids = request.data.get('delete_ids',[])

         # Convert delete_ids to a list of integers
         delete_ids = [int(id) for id in delete_ids]
         
         if delete_ids:
            todo = ToDo.objects.filter(id__in=delete_ids)
            if todo.exists():
               todo.delete()
               return Response({'message': 'Tasks deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
               return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

         else:
            todos = ToDo.objects.all()
            if todos.exists():

              todos.delete()
              return Response({'message': 'All Tasks deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
               return Response({'message': 'no tasks found'}, status=status.HTTP_404_NOT_FOUND)

                           
      except ToDo.DoesNotExist:
         return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
                
            
      
            
       
      