from core.renderers import BaseJSONRenderer


class CategoryJSONRenderer(BaseJSONRenderer):
    object_label = 'category'


class LanguageJSONRenderer(BaseJSONRenderer):
    object_label = 'language'


class AuthorJSONRenderer(BaseJSONRenderer):
    object_label = 'author'


class BookJSONRenderer(BaseJSONRenderer):
    object_label = 'book'


class CommentJSONRenderer(BaseJSONRenderer):
    object_label = 'comment'
