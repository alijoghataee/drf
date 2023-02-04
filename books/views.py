from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from .models import Book
from .serializers import BookModelSerializer, BookSerializer


class ListAndCreateData(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    permission_classes = [IsAuthenticated]


class RetrieveApi(mixins.CreateModelMixin, generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GetAllDate(APIView):
    def get(self, request):
        query = Book.objects.all()
        serializer = BookModelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailApi(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class PostModelDate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostData(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            author = serializer.data.get('author')
            story_name = serializer.data.get('story_name')
            description = serializer.data.get('description')
            image = request.FILES['image']
            fav = serializer.data.get('fav')
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        book = Book()
        book.author = author
        book.story_name = story_name
        book.description = description
        book.image = image
        book.fav = fav
        book.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SearchData(APIView):
    def get(self, request):
        search = request.GET['name']
        query = Book.objects.filter(story_name__contains=search)
        serializer = BookModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangeData(APIView):
    def get(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializer = BookModelSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Book.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializer = BookModelSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_api(request):
    if request.method == 'GET':
        query = Book.objects.all()
        serializer = BookModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_api(request):
    if request.method == 'POST':
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def change_api(request, pk):
    if request.method == 'PUT':
        query = Book.objects.get(pk=pk)
        serializer = BookModelSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
    else:
        query = Book.objects.get(pk=pk)
        serializer = BookModelSerializer(query)
    return Response(serializer.data, status=status.HTTP_200_OK)
