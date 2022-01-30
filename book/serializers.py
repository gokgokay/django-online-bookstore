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


class BookSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True, read_only=True)
    categories = serializers.CharField()
    authors = serializers.CharField()

    class Meta:
        model = Book
        exclude = ['image', 'slug']


class CommentSerializer(serializers.ModelSerializer):
    books = serializers.CharField()
    users = serializers.CharField()
    rate = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Comment
        fields = ['books', 'users', 'comment', 'rate']
