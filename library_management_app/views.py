from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from library_management_app.models import Book
from django.http import HttpRequest
from django.http import HttpResponse
from .models import Author
from .permission import IsAdminOrReadOnly
from .serializers import AuthorSerializer
from .serializers import BookSerializer
from .filters import AuthorFilter, BookFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
#
# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetail(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['first_name', 'last_name']
    permission_classes = [IsAdminOrReadOnly]


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['first_name', 'last_name']
    permission_classes = [IsAuthenticated]


def send_mail_function(request):
    try:
        send_mail("Library message", "Your book order is now available", "ikunbomorin@gmail.com", ["zainab@gmail.com"])
    except BadHeaderError:
        pass
    return HttpResponse('ok')

    # def get_serializer_context(self):
    #     return {"request": self.request}

# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# # CLass Based View
# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

#     def get_queryset(self):
#         return Author.objects.all()
#
#     def get_serializer_class(self):
#         return AuthorSerializer


# class AuthorView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializers = AuthorSerializer(authors, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("success", status=status.HTTP_200_OK)
#
#
# class AuthorDetailView(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("detail updated", status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         if author.book_set.count() > 0:
#             return Response({"error": "Auth0r associated with book cannot be deleted"},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#         author.delete()
#         return Response("Successfully deleted", status=status.HTTP_204_NO_CONTENT)
#

# Function based view
# @api_view(['GET', 'POST'])
# def list_authors(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializers = AuthorSerializer(authors, many=True)
#         return Response(serializers.data, status.HTTP_200_OK)
#     elif request.method == 'POST':
#         deserialize = AuthorSerializer(data=request.data)
#         deserialize.is_valid(raise_exception=True)
#         # deserialize.validated_data()
#         deserialize.save()
#         return Response("Success", status=status.HTTP_201_CREATED)
#     # return render(request, 'book/author-list.html', {'authors': authors})


# @api_view()
# def welcome(request):
#     return Response('OK')
#
#
# @api_view()
# def welcome_you(request):
#     return Response('You are welcome in the name of the Lord')
#

# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = Author.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("detail updated", status=status.HTTP_200_OK)
#
#     elif request.method == 'DELETE':
#         if author.book_set.count() > 0:
#             return Response({"error": "Auth0r associated with book cannot be deleted"},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         author.delete()
#         return Response("Successfully deleted", status=status.HTTP_204_NO_CONTENT)


#     return render(request, 'book/books-available.html', {'available_books': books})


# @api_view(['GET', 'POST'])
# def list_books(request):
#     books = Book.objects.all()
#     if request.method == 'GET':
#         serializer = BookSerializer(books, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serialize = BookSerializer(data=request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response("Success", status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     books = Book.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(books, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = BookSerializer(books, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Detail Updated", status=status.HTTP_200_OK)
#
#     elif request.method == 'DELETE':
#         if books.book_set.count() > 0:
#             return Response({"error": "Book cannot be deleted"},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         books.delete()
#         return Response("Successfully deleted", status=status.HTTP_204_NO_CONTENT)

# @api_view()
# def author_detail(request, pk):
#     # author = get_object_or_404()
#     return Response(pk)
# #     return render(request, 'book/books-available.html', {'available_books': books})
