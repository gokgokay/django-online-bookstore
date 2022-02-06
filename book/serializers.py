from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Author, Book, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']


class BookSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True, read_only=True)
    categories = serializers.StringRelatedField(read_only=True)
    authors = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        exclude = ['image', 'slug', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(read_only=True)
    users = serializers.StringRelatedField(read_only=True)
    rate = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Comment
        fields = ['id', 'books', 'users', 'comment', 'rate']
