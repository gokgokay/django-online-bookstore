from django.contrib import admin
from book.models import Category, Author, Book, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['rate']
