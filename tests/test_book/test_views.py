import json
import factory
from django.db.models import signals


class TestCategoryListAPIView:

    def test_list(self, db, api_client, category_factory, check):
        endpoint = '/api/category/'
        category_factory.create_batch(5)
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['categories']))

    def test_empty_list(self, db, api_client, category_factory, check):
        endpoint = '/api/category/'
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(0, len(json.loads(response.content)['categories']))


class TestLanguageListAPIView:

    def test_list(self, db, api_client, language_factory, check):
        endpoint = '/api/language/'
        language_factory.create_batch(5)
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['languages']))

    def test_empty_list(self, db, api_client, language_factory, check):
        endpoint = '/api/language/'
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(0, len(json.loads(response.content)['languages']))


class TestAuthorListAPIView:

    def test_list(self, db, api_client, author_factory, check):
        endpoint = '/api/author/'
        author_factory.create_batch(5)
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['authors']))

    def test_empty_list(self, db, api_client, author_factory, check):
        endpoint = '/api/author/'
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(0, len(json.loads(response.content)['authors']))


class TestBookListAPIView:

    def test_list(self, db, api_client, book_factory, check):
        endpoint = '/api/book/'
        book_factory.create_batch(5)
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['books']))

    def test_empty_list(self, db, api_client, book_factory, check):
        endpoint = '/api/book/'
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(0, len(json.loads(response.content)['books']))


class TestCommentsListCreateAPIView:

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_list(self, db, api_client, comment_factory, check):
        endpoint = '/api/book/<book_slug>/comment/'
        comment_factory.create_batch(5)
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['comments']))

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_empty_list(self, db, api_client, comment_factory, check):
        endpoint = '/api/book/<book_slug>/comment/'
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(0, len(json.loads(response.content)['comments']))

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_create(self, db, api_client, comment_factory, book_factory, profile_factory, check):
        book = book_factory()
        profile = profile_factory()
        comment = comment_factory.build(book=book, profile=profile)
        endpoint = f'/api/book/{comment.book.slug}/comment/'

        data = {
            'book': comment.book.id,
            'profile': comment.profile.id,
            'body': comment.body
        }

        api_client.force_authenticate(comment.profile.user)
        response = api_client.post(endpoint, data=data, format='json')

        expected_data = {
            'status': response.status_code,
            'comments':
                {
                    'book': comment.book.name,
                    'profile': comment.profile.user.username,
                    'body': comment.body
                }
        }

        check.equal(200, response.status_code)
        check.equal(expected_data, json.loads(response.content))


class TestCommentUpdateDestroyAPIView:

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_update(self, db, api_client, comment_factory, book_factory, profile_factory, check, faker):
        book = book_factory()
        profile = profile_factory()
        comment = comment_factory.create(book=book, profile=profile)
        endpoint = f'/api/book/{comment.book.slug}/comment/{comment.pk}/'

        data = {
            'book': comment.book.id,
            'profile': comment.profile.id,
            'body': faker.text(),
        }

        api_client.force_authenticate(comment.profile.user)
        response = api_client.patch(endpoint, data=data, format='json')

        expected_data = {
            'profile': response.data['profile'],
            'book': response.data['book'],
            'body': response.data['body'],
        }

        check.equal(200, response.status_code)
        check.equal(expected_data, json.loads(response.content))

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_destroy(self, db, api_client, comment_factory, book_factory, profile_factory, check):
        book = book_factory()
        profile = profile_factory()
        comment = comment_factory.create(book=book, profile=profile)
        endpoint = f'/api/book/{comment.book.slug}/comment/{comment.pk}/'
        api_client.force_authenticate(comment.profile.user)
        response = api_client.delete(endpoint)

        check.equal(204, response.status_code)
