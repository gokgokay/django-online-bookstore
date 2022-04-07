import json
import factory
from django.db.models import signals


class TestCategoryListAPIView:
    endpoint = '/api/category/'

    def test_list(self, db, api_client, category_factory, check):
        category_factory.create_batch(5)
        response = api_client().get(self.endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['categories']))


class TestLanguageListAPIView:
    endpoint = '/api/language/'

    def test_list(self, db, api_client, language_factory, check):
        language_factory.create_batch(5)
        response = api_client().get(self.endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['languages']))


class TestAuthorListAPIView:
    endpoint = '/api/author/'

    def test_list(self, db, api_client, author_factory, check):
        author_factory.create_batch(5)
        response = api_client().get(self.endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['authors']))


class TestBookListAPIView:
    endpoint = '/api/book/'

    def test_list(self, db, api_client, book_factory, check):
        book_factory.create_batch(5)
        response = api_client().get(self.endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['books']))


class TestCommentsListCreateAPIView:

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_list(self, db, api_client, comment_factory, check):
        endpoint = '/api/book/<book_slug>/comment/'
        comment_factory.create_batch(5)
        response = api_client().get(endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['comments']))

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_create(self, db, api_client, comment_factory, check, user_factory):
        pass
