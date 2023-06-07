from decimal import Decimal

from rest_framework import serializers
from .models import Author
from .models import Book
from djoser.serializers import UserSerializer as CurrentUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']
    # first_name = serializers.CharField(max_length=255)
    # last_name = serializers.CharField(max_length=255)
    # date_of_birth = serializers.DateField()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'date_added', 'book_number', 'discount_price', 'author']

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author-detail'
    )

    book_number = serializers.CharField(max_length=33, source='isbn')
    discount_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, book: Book):
        return book.price * Decimal(0.1)
    # title = serializers.CharField(max_length=255)
    # description = serializers.CharField(max_length=255)
    # date_added = serializers.DateTimeField()
    # author = serializers.ForeignKey(Author, on_delete=models.CASCADE)
    # genre = serializers.CharField(max_length=10, choices=GENRE_CHOICES)
    # language = serializers.CharField(max_length=10, choices=LANGUAGE_MODELS)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class UserSerializer(CurrentUserSerializer):
    class Meta(CurrentUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'firstname', 'lastname']
