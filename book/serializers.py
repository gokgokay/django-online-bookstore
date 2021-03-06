from rest_framework import serializers
from .models import Category, Author, Book, Comment, Language


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'bio']


class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    author = serializers.CharField(read_only=True)
    language = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(required=False)
    comments = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Book
        fields = [
            'author',
            'category',
            'slug',
            'price',
            'stock',
            'available',
            'language',
            'comments',
            'description', ]


class FavoriteBookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        fields = ['name', 'author']


class CommentSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField(read_only=True)
    book = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['profile', 'book', 'body']

    def create(self, validated_data):
        book = self.context['book']
        profile = self.context['profile']

        return Comment.objects.create(book=book, profile=profile, **validated_data)
