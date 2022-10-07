from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from base.models import Task
from.serializers import PostSerializer


@api_view(['GET'])
def getRoutes(request):
    tasks = [
        'GET /api',
        'GET /api/tasks',
        'GET /api/tasks/:id'
    ]
    return Response(tasks)


@api_view(['GET', 'POST'])
def get_task(request, format=None):

    if request.method == 'GET':
        post = Task.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def getTask(request, pk, format=None):

    try:
        posts = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(posts, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    

    