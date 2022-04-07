import json


class TestCategoryListAPIView:
    endpoint = '/api/category/'

    def test_list(self, db, api_client, category_factory, check):
        category = category_factory.create_batch(5)
        response = api_client().get(self.endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['categories']))


class TestLanguageListAPIView:
    endpoint = '/api/language/'

    def test_list(self, db, api_client, language_factory, check):
        language = language_factory.create_batch(5)
        response = api_client().get(self.endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['languages']))
