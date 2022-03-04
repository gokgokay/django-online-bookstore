from rest_framework import serializers
from .models import Category, Author, Book, Comment, Language


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']


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
            'description',
            'created_at',
            'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'profile', 'body']

    def create(self, validated_data):
        book = self.context['book']
        profile = self.context['profile']

        return Comment.objects.create(book=book, profile=profile, **validated_data)
