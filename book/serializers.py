from rest_framework import serializers
from .models import Category, Author, Book, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'bio']


class CommentSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        exclude = ['books']


class BookSerializer(serializers.ModelSerializer):
    #comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        exclude = ['image', 'slug']
